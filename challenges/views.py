import requests
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Problem, Submission
from .serializers import ProblemSerializer


class UserProgressAPI(APIView):
    """
    API to fetch user's completed problem IDs.
    """
    def get(self, request):
        clerk_id = request.query_params.get('clerk_id')
        
        if not clerk_id:
            return Response({"completed": []})
        
        try:
            user = User.objects.get(username=clerk_id)
            # Get unique problem IDs that user has passed
            completed_ids = list(
                Submission.objects.filter(user=user, status="Passed")
                .values_list('problem_id', flat=True)
                .distinct()
            )
            return Response({"completed": completed_ids})
        except User.DoesNotExist:
            return Response({"completed": []})

class ProblemListAPI(APIView):
    """
    API to fetch the list of all problems for the frontend.
    """
    def get(self, request):
        problems = Problem.objects.all()
        serializer = ProblemSerializer(problems, many=True)
        return Response(serializer.data)

class ExecuteCodeAPI(APIView):
    """
    API to execute user code, provide smart hints, and SAVE progress.
    """
    def post(self, request):
        # 1. Get data from Frontend
        code = request.data.get('code')
        language = request.data.get('language', 'python')
        problem_id = request.data.get('problem_id')
        
        # 2. Get the real problem from DB
        try:
            problem = Problem.objects.get(id=problem_id)
        except Problem.DoesNotExist:
            return Response({"error": "Problem not found"}, status=404)
            
        # 3. Loop through test cases
        test_cases = problem.test_cases
        results = []
        all_passed = True
        
        for case in test_cases:
            # Prepare payload for Piston API
            payload = {
                "language": language,
                "version": "*",
                "files": [{"content": code}],
                "stdin": case['input']
            }
            
            try:
                # Send to Piston
                response = requests.post('https://emkc.org/api/v2/piston/execute', json=payload)
                data = response.json()
            except Exception as e:
                return Response({"status": "Error", "message": "Compiler Service Unavailable"}, status=503)
            
            # Clean outputs
            user_output = data.get('run', {}).get('stdout', '').strip()
            expected_output = case['output'].strip()
            
            passed = (user_output == expected_output)
            feedback = None
            
            # --- SMART HINT LOGIC ---
            if not passed:
                all_passed = False
                if user_output.lower() == expected_output.lower():
                    feedback = "⚠️ Case Mismatch: Check your capitalization!"
                elif user_output.replace(" ", "") == expected_output.replace(" ", ""):
                    feedback = "⚠️ Spacing Issue: Check for extra spaces or newlines."
            # ------------------------

            results.append({
                "input": case['input'],
                "expected": expected_output,
                "actual": user_output,
                "passed": passed,
                "feedback": feedback
            })
            
            # Stop if failed (optional)
            if not passed:
                break
        
        # ... (Previous code remains the same) ...

        # 4. FINAL VERDICT & SAVING
        if all_passed:
            # A. Calculate Points
            points_map = {'BEG': 10, 'INT': 20, 'ADV': 35, 'PRO': 50}
            earned_points = points_map.get(problem.difficulty, 10)
            
            # B. FIND OR CREATE USER
            clerk_id = request.data.get('clerk_id')
            email = request.data.get('email')
            user = None

            if clerk_id:
                # Magic Line: Get the user if they exist, OR create them if they don't!
                user, created = User.objects.get_or_create(
                    username=clerk_id,  # We use Clerk ID as the unique username
                    defaults={'email': email}
                )

            # C. Save Submission
            if user:
                Submission.objects.create(
                    user=user,
                    problem=problem,
                    code=code,
                    language=language,
                    status="Passed"
                )
            
            return Response({
                "status": "Success", 
                "results": results, 
                "points": earned_points 
            })
        else:
            # Return failed response when tests don't pass
            return Response({
                "status": "Failed",
                "results": results
            })