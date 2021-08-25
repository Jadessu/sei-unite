from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def home(request):
     return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


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

    

class ProjectDelete(DeleteView):
    model = Project
    success_url = '/projects/'