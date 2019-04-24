from django.shortcuts import render

from .models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'portfolio/index.html', context)

def project_details(request, slug):
    project = Project.objects.get(slug=slug)
    context = { 'project': project }
    return render(request, 'portfolio/detail.html', context)
