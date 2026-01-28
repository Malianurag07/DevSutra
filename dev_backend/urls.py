from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# Import all API views
from challenges.views import ProblemListAPI, ExecuteCodeAPI, UserProgressAPI

def home(request):
    return HttpResponse("Welcome to the DevSutra Backend!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/problems/', ProblemListAPI.as_view()),
    path('api/execute/', ExecuteCodeAPI.as_view()),
    path('api/progress/', UserProgressAPI.as_view()),  # User's completed problems
    path('', home), 
]