from django.shortcuts import render
from .models import Project

projectsList = [
    {
        'id': '1',
        'title': 'Work Flow Automation',
        'description': 'Real-world project at Peoples Group'
    },
    {
        'id': '2',
        'title': 'Django',
        'description': 'Something useful for me to use'
    },
    {
        'id': '3',
        'title': 'API Integration on Upwork',
        'description': 'Making some real $$$ with my programming skills'
    }
]


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    context2 = {'project': projectObj}
    print({'project': projectObj})
    return render(request, 'projects/single_project.html', context2)