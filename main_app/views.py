from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
     return render('home.html')

def about(request):
    return render(request, 'about.html')




def projects_index(request):
    return render(request, 'projects/index.html', {'projects': projects})