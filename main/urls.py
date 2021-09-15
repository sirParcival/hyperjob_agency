from django.urls import path
from .views import Menu, Login, Signup, Home

urlpatterns = [
    path('', Menu.as_view(), name='menu'),
    path('login', Login.as_view(), name='login'),
    path('signup', Signup.as_view(), name='signup'),
    path('home/', Home.as_view(), name='home')
]
