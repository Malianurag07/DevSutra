from rest_framework import serializers
from .models import Problem, Submission

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        # Include test_cases for showing expected output examples
        fields = ['id', 'title', 'description', 'difficulty', 'starter_code', 'real_life_context', 'explanation', 'solutions', 'test_cases']

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'