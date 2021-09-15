from django.shortcuts import render
from django import views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView


# Create your views here.
class Menu(views.View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Signup(views.generic.CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'


class Login(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'

class Home(views.generic.base.TemplateView):
    template_name = "home.html"
