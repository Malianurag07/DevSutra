from django.db import models

class Problem(models.Model):
    DIFFICULTY_CHOICES = [
        ('BEG', 'Beginner'),
        ('INT', 'Intermediate'),
        ('ADV', 'Advanced'),
        ('PRO', 'Pro'),
    ]

    title = models.CharField(max_length=200, unique=True) # Unique to avoid duplicates
    description = models.TextField()
    difficulty = models.CharField(max_length=3, choices=DIFFICULTY_CHOICES)
    real_life_context = models.TextField(blank=True, null=True)
    explanation = models.TextField(blank=True, null=True) # AI Explanation

    # Stores starter code for: python, c, cpp, java
    starter_code = models.JSONField(default=dict) 
    
    # Stores correct solution for: python, c, cpp, java
    solutions = models.JSONField(default=dict)
    
    # Stores input/output cases
    test_cases = models.JSONField(default=list)

    def __str__(self):
        return f"[{self.difficulty}] {self.title}"

class Submission(models.Model):
    from django.contrib.auth.models import User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField()
    language = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)