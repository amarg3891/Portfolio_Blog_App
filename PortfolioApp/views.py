from django.shortcuts import render
from .models import Project,Service


# View Function Render the Model Objects to Webpage.
def project_index(request):
    projects = Project.objects.all()
    services = Service.objects.all()

    return render(request, 'PortfolioApp/portfolio.html',{'projects': projects,'services':services})

# This Function contains project details
def project_detail(request,pk):
    
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'PortfolioApp/project_detail.html', context)

# Service Function
def service_detail(request,pk):
    service = Service.objects.get(pk=pk)
    return render(request, 'PortfolioApp/service_detail.html', {'service':service})