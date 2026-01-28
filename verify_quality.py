"""Full quality verification"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dev_backend.settings')
django.setup()

from challenges.models import Problem

print("="*60)
print("FINAL QUALITY VERIFICATION")
print("="*60)

levels = [('BEG', 'Beginner'), ('INT', 'Intermediate'), ('ADV', 'Advanced'), ('PRO', 'Professional')]

for code, name in levels:
    problems = Problem.objects.filter(difficulty=code)
    total = problems.count()
    
    no_solution = 0
    no_explanation = 0
    no_context = 0
    
    for p in problems:
        sol = p.solutions.get('python', '') if p.solutions else ''
        if not sol or len(sol.strip()) < 30:
            no_solution += 1
        if not p.explanation or len(p.explanation.strip()) < 20:
            no_explanation += 1
        if not p.real_life_context or len(p.real_life_context.strip()) < 20:
            no_context += 1
    
    print(f"\n{name} ({code}): {total} problems")
    print(f"  Need solutions: {no_solution}")
    print(f"  Need explanations: {no_explanation}")
    print(f"  Need real-life context: {no_context}")

total_all = Problem.objects.count()
print(f"\n{'='*60}")
print(f"TOTAL: {total_all} problems")
print("="*60)
