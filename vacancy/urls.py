from django.urls import path
from .views import Vacancies, New

urlpatterns = [
    path('vacancies/', Vacancies.as_view(), name='vacancies'),
    path('vacancy/new', New.as_view()),
]