from django.shortcuts import render
from django.views.generic import ListView
from .models import Project

# def project_view(request): 
#     return render(request, 'project/portfolio-overview.html')

class ProjectListView(ListView):
    model = Project
    template_name = 'project/portfolio-overview.html'
    