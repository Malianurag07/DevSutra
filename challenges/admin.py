from django.contrib import admin
from .models import Problem, Submission

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    # Removed 'created_at' because it's not in your new model
    list_display = ('title', 'difficulty', 'id') 
    list_filter = ('difficulty',)
    search_fields = ('title', 'description')

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    # Changed 'submitted_at' to 'created_at' to match your model
    list_display = ('user', 'problem', 'status', 'language', 'created_at')
    list_filter = ('status', 'language', 'created_at')