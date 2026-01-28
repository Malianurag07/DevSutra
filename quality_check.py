"""Check and report on problem quality"""
import os
import sys
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dev_backend.settings')
django.setup()

from challenges.models import Problem

print("="*60)
print("PROBLEM QUALITY REPORT")
print("="*60)

levels = ['BEG', 'INT', 'ADV', 'PRO']
for level in levels:
    problems = Problem.objects.filter(difficulty=level)
    total = problems.count()
    
    incomplete = 0
    for p in problems:
        sol = p.solutions.get('python', '') if p.solutions else ''
        if not sol or 'pass' in sol or len(sol) < 30:
            incomplete += 1
    
    print(f"{level}: {total} total, {incomplete} need better solutions")

print("="*60)
