"""Fix problems with placeholder solutions by deleting them"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dev_backend.settings')
django.setup()

from challenges.models import Problem

print("Fixing problems with placeholder solutions...\n")

deleted_count = 0
for level in ['BEG', 'INT', 'ADV', 'PRO']:
    problems = Problem.objects.filter(difficulty=level)
    for p in problems:
        sol = p.solutions.get('python', '') if p.solutions else ''
        # Delete problems with placeholder solutions
        if not sol or len(sol.strip()) < 30 or 'pass' in sol or '# Solution for' in sol or '# Implementation depends' in sol:
            print(f"  Deleting: {p.title[:50]}...")
            p.delete()
            deleted_count += 1

print(f"\nDeleted {deleted_count} problems with placeholder solutions.")

# Show final counts
print("\nFinal counts:")
for code in ['BEG', 'INT', 'ADV', 'PRO']:
    count = Problem.objects.filter(difficulty=code).count()
    status = "✅" if count >= 250 else "⚠️ Need more"
    print(f"  {code}: {count} {status}")
