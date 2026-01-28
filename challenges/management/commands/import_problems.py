import json
import os
from django.core.management.base import BaseCommand
from challenges.models import Problem


class Command(BaseCommand):
    help = 'Import problems from JSON files into the database'

    def add_arguments(self, parser):
        parser.add_argument(
            'difficulty',
            type=str,
            nargs='?',
            default='all',
            help='Difficulty level to import: beginner, intermediate, advanced, pro, or all'
        )
        parser.add_argument(
            '--limit',
            type=int,
            default=None,
            help='Limit number of problems to import (for testing)'
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Validate JSON without importing'
        )

    def handle(self, *args, **kwargs):
        difficulty = kwargs['difficulty'].lower()
        limit = kwargs['limit']
        dry_run = kwargs['dry_run']

        # Map difficulty names to codes
        difficulty_map = {
            'beginner': 'BEG',
            'intermediate': 'INT',
            'advanced': 'ADV',
            'pro': 'PRO',
            'all': None
        }

        if difficulty not in difficulty_map:
            self.stdout.write(self.style.ERROR(
                f'Invalid difficulty: {difficulty}. Use: beginner, intermediate, advanced, pro, or all'
            ))
            return

        # Get data directory path
        data_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
        data_dir = os.path.normpath(data_dir)

        if not os.path.exists(data_dir):
            self.stdout.write(self.style.ERROR(f'Data directory not found: {data_dir}'))
            return

        # Determine which files to import
        if difficulty == 'all':
            files_to_import = [
                ('problems_beginner.json', 'BEG'),
                ('problems_intermediate.json', 'INT'),
                ('problems_advanced.json', 'ADV'),
                ('problems_pro.json', 'PRO'),
            ]
        else:
            files_to_import = [
                (f'problems_{difficulty}.json', difficulty_map[difficulty])
            ]

        total_imported = 0
        total_skipped = 0
        total_errors = 0

        for filename, diff_code in files_to_import:
            filepath = os.path.join(data_dir, filename)
            
            if not os.path.exists(filepath):
                self.stdout.write(self.style.WARNING(f'File not found: {filename} - skipping'))
                continue

            self.stdout.write(f'\n📂 Processing: {filename}')

            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    problems_data = json.load(f)
            except json.JSONDecodeError as e:
                self.stdout.write(self.style.ERROR(f'Invalid JSON in {filename}: {e}'))
                total_errors += 1
                continue

            if not isinstance(problems_data, list):
                self.stdout.write(self.style.ERROR(f'{filename} should contain a JSON array'))
                total_errors += 1
                continue

            # Apply limit if specified
            if limit:
                problems_data = problems_data[:limit]

            for idx, problem in enumerate(problems_data):
                # Validate required fields
                required_fields = ['title', 'description', 'starter_code', 'solutions', 'test_cases']
                missing = [f for f in required_fields if f not in problem]
                
                if missing:
                    self.stdout.write(self.style.WARNING(
                        f'  ⚠️ Problem {idx+1}: Missing fields: {missing} - skipping'
                    ))
                    total_errors += 1
                    continue

                # Check for duplicate title
                if Problem.objects.filter(title=problem['title']).exists():
                    self.stdout.write(self.style.WARNING(
                        f'  ⏭️ Duplicate: "{problem["title"][:40]}..." - skipping'
                    ))
                    total_skipped += 1
                    continue

                if dry_run:
                    self.stdout.write(self.style.SUCCESS(
                        f'  ✓ Valid: "{problem["title"][:50]}..."'
                    ))
                    total_imported += 1
                    continue

                # Create the problem
                try:
                    Problem.objects.create(
                        title=problem['title'],
                        description=problem['description'],
                        difficulty=diff_code,
                        real_life_context=problem.get('real_life_context', ''),
                        explanation=problem.get('explanation', ''),
                        starter_code=problem.get('starter_code', {}),
                        solutions=problem.get('solutions', {}),
                        test_cases=problem.get('test_cases', [])
                    )
                    total_imported += 1
                    self.stdout.write(self.style.SUCCESS(
                        f'  ✅ Imported: "{problem["title"][:50]}..."'
                    ))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(
                        f'  ❌ Error importing "{problem["title"][:30]}...": {e}'
                    ))
                    total_errors += 1

        # Summary
        self.stdout.write('\n' + '='*50)
        action = 'validated' if dry_run else 'imported'
        self.stdout.write(self.style.SUCCESS(f'✅ {total_imported} problems {action}'))
        self.stdout.write(self.style.WARNING(f'⏭️ {total_skipped} duplicates skipped'))
        self.stdout.write(self.style.ERROR(f'❌ {total_errors} errors'))
        self.stdout.write('='*50)
