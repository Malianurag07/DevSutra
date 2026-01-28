import json
import time
import requests
import google.generativeai as genai
from django.core.management.base import BaseCommand
from challenges.models import Problem

# --- CONFIGURATION ---
# PASTE YOUR KEY HERE
GOOGLE_API_KEY = "AIzaSyBUm-rdfIy1C2j-KS_zwuF4VIknzVXbQrA"  
genai.configure(api_key=GOOGLE_API_KEY)
MODEL_NAME = 'gemini-flash-latest' # The reliable free model (15 RPM)

class Command(BaseCommand):
    help = 'Generates Verified Coding Problems'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Target number of VALID problems')
        parser.add_argument('difficulty', type=str, help='BEG, INT, ADV, PRO')

    def verify_logic(self, code, test_cases):
        """Runs the Python code against Piston to ensure it PRINTS the right answer."""
        if not code or not test_cases:
            return False, "Empty code"

        for case in test_cases:
            payload = {
                "language": "python", "version": "3.10.0",
                "files": [{"content": code}], "stdin": case['input']
            }
            try:
                response = requests.post('https://emkc.org/api/v2/piston/execute', json=payload)
                result = response.json()
                
                if result.get('run', {}).get('stderr'):
                     return False, f"Syntax Error: {result['run']['stderr']}"

                run_output = result.get('run', {}).get('stdout', '').strip()
                expected = case['output'].strip()
                
                if run_output != expected:
                    return False, f"Mismatch! Input: {case['input']} | Exp: '{expected}' | Got: '{run_output}'"
            except Exception as e:
                return False, f"API Error: {e}"
        return True, "Passed"

    def handle(self, *args, **kwargs):
        target_count = kwargs['count']
        difficulty = kwargs['difficulty']
        model = genai.GenerativeModel(MODEL_NAME)
        
        self.stdout.write(f"🛡️  Starting Exponential Backoff Factory ({difficulty})...")
        
        valid_problems = 0
        backoff_time = 60 # Start with 60 seconds wait on error

        while valid_problems < target_count:
            # Base Safety Sleep: 20s (3 RPM) to be super safe
            time.sleep(20) 

            prompt = f"""
            Task: Generate 1 coding problem for {difficulty} level.
            Strict Output: JSON ONLY.
            
            CRITICAL RULES FOR SOLUTIONS:
            1. The "python" solution MUST read from 'input()' and PRINT the result.
            2. Do NOT just return a value. If you don't print, the test fails.
            3. Example Python Solution:
               n = int(input())
               print(n * 2)
            4. **NO FLOATING POINT MATH.** Use Integers or Strings only. 

            Structure:
            {{
                "title": "Unique Title",
                "description": "Task description",
                "explanation": "Logic explanation",
                "real_life_context": "Why it matters",
                "starter_code": {{ "python": "# Write your code here", "java": "...", "c": "...", "cpp": "..." }},
                "solutions": {{ 
                    "python": "import sys\\n# Full working script\\n...", 
                    "java": "...", "c": "...", "cpp": "..." 
                }},
                "test_cases": [ {{ "input": "...", "output": "..." }} ]
            }}
            """

            try:
                response = model.generate_content(prompt)
                raw = response.text.replace("```json", "").replace("```", "").strip()
                data = json.loads(raw)

                if not all(k in data['solutions'] for k in ['python', 'java', 'c', 'cpp']):
                    self.stdout.write(self.style.WARNING(f"⚠️  Discarded: Missing Languages"))
                    continue

                if Problem.objects.filter(title=data['title']).exists():
                    self.stdout.write(self.style.WARNING(f"⚠️  Duplicate skipped"))
                    continue

                is_valid, reason = self.verify_logic(data['solutions']['python'], data['test_cases'])
                
                if is_valid:
                    Problem.objects.create(
                        title=data['title'],
                        description=data['description'],
                        difficulty=difficulty,
                        real_life_context=data.get('real_life_context', ''),
                        explanation=data.get('explanation', ''),
                        starter_code=data['starter_code'],
                        solutions=data['solutions'],
                        test_cases=data['test_cases']
                    )
                    valid_problems += 1
                    backoff_time = 60 # Reset backoff on success
                    self.stdout.write(self.style.SUCCESS(f"✅ [{valid_problems}/{target_count}] Saved: {data['title']}"))
                else:
                    self.stdout.write(self.style.WARNING(f"❌ Logic Check Failed: {reason}"))

            except Exception as e:
                error_msg = str(e)
                if "429" in error_msg or "Quota exceeded" in error_msg:
                    self.stdout.write(self.style.ERROR(f"🛑 Rate Limit Hit! Cooling down {backoff_time}s..."))
                    # If we are hitting limits, PRINT the error so we know if it is Daily Limit
                    if "limit: 0" in error_msg:
                         self.stdout.write(self.style.ERROR("CRITICAL: Daily Limit or Model Ban Detected."))
                    
                    time.sleep(backoff_time)
                    backoff_time *= 2 # Double the wait time for next failure (Exponential Backoff)
                    if backoff_time > 600: backoff_time = 600 # Cap at 10 minutes
                else:
                    self.stdout.write(self.style.ERROR(f"💥 Error: {e}"))
                    time.sleep(5)

        self.stdout.write(self.style.SUCCESS(f"🎉 DONE! Generated {valid_problems} problems."))