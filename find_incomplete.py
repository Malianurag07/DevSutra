"""Find and list problems that need better solutions"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dev_backend.settings')
django.setup()

from challenges.models import Problem

print("Problems needing better solutions:\n")

for level in ['BEG', 'INT', 'ADV', 'PRO']:
    problems = Problem.objects.filter(difficulty=level)
    incomplete = []
    for p in problems:
        sol = p.solutions.get('python', '') if p.solutions else ''
        if not sol or len(sol.strip()) < 30 or 'pass' in sol or '# Solution' in sol:
            incomplete.append((p.id, p.title, sol[:50] if sol else 'None'))
    
    if incomplete:
        print(f"\n{level} Level ({len(incomplete)} problems):")
        for id, title, sol_preview in incomplete:
            print(f"  ID {id}: {title[:40]}... | Sol: {sol_preview}...")
