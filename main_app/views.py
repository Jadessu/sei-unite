from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Alumnus
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView


# Create your views here.
class Home(LoginView):
     template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

# ------------------------------------ALUMNUS---------------------------------------------------------
def alumnus_index(request):
    alumnus = Alumnus.objects.all()
    return render(request, 'alumnus/index.html', {'alumnus': alumnus})

def alumnus_detail(request, alumnus_id):
    alumnus = Alumnus.objects.get(id=alumnus_id)
    return render(request, 'alumnus/detail.html', {'alumnus': alumnus})

class AlumnusCreate(CreateView):
    model = Alumnus
    fields = '__all__'
    success_url = '/alumnus/'

class AlumnusUpdate(UpdateView):
    model = Alumnus
    fields = '__all__'
    success_url = '/alumnus/'

class AlumnusDelete(DeleteView):
    model = Alumnus
    success_url = '/alumnus/'
# ------------------------------------PROJECTS----------------------------------------------------------
def projects_index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})

def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'projects/detail.html', {'project': project})

class ProjectCreate(CreateView):
    model = Project
    fields = '__all__'
    success_url = '/projects/'

class ProjectUpdate(UpdateView):
    model = Project
    fields = ['completed', 'image', 'lookingfor']
    success_url = '/projects/'
   

class ProjectDelete(DeleteView):
    model = Project
    success_url = '/projects/'

