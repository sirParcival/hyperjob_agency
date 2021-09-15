from django.shortcuts import render, redirect
from django import views
from .models import Resume

from django.http import HttpResponseForbidden


class Resumes(views.View):
    template_name = "resume.html"

    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, self.template_name, {'resumes': resumes})


class New(views.View):

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            Resume.objects.create(description=request.POST.get('description'), author=request.user)
            return redirect('home')
        else:
            return HttpResponseForbidden()
