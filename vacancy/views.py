from django.shortcuts import render, redirect
from django import views
from .models import Vacancy
from django.http import HttpResponseForbidden

# Create your views here.
class Vacancies(views.View):
    template_name = "vacancy.html"

    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, self.template_name, {'vacancies': vacancies})

class New(views.View):

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            Vacancy.objects.create(description=request.POST.get('description'), author=request.user)
            return redirect('home')
        else:
            return HttpResponseForbidden()
