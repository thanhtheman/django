from django.shortcuts import render

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
    msg = 'Thanh is a talented programmer.'
    number = 11
    context = {'message': msg, 'number': number}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    return render(request, 'projects/single_project.html')