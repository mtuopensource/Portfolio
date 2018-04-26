from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects
    return render(request, 'home.html', {'projects': projects})

def description(request, id):
    project = get_object_or_404(Project, id = id)
    return render(request, 'description.html', {'project': project})
