from django.urls import path
from .views import Resumes, New

urlpatterns = [
    path('resumes/', Resumes.as_view(), name='resumes'),
    path('resume/new', New.as_view()),
]