from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Alumnus
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


# Create your views here.
def home(request):
     return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# ------------------------------------ALUMNUS---------------------------------------------------------
def alumnus_index(request):
    alumnus = Alumnus.objects.all()
    return render(request, 'alumnus/index.html', {'alumnus': alumnus})

def alumnus_detail(request, alumnus_id):
    alumnus = Alumnus.objects.get(id=alumnus_id)
    return render(request, 'alumnus/detail.html', {'alumnus': alumnus})
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

