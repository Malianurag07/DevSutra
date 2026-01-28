from challenges.models import Problem

problems = Problem.objects.filter(difficulty='BEG').order_by('-id')[:10]
for p in problems:
    sol = p.solutions.get('python', '') if p.solutions else ''
    print(f"ID: {p.id}")
    print(f"Title: {p.title}")
    print(f"Has Solution: {bool(sol and 'pass' not in sol and len(sol) > 20)}")
    print(f"Solution: {sol[:100]}...")
    print("-" * 50)
