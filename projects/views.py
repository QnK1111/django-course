from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Review, Tag
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def projects(request):
    projs = Project.objects.all()
    return render(request, 'projects/projects.html', {'projectsList':projs})

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    context = {
        'project' : projectObj,
        }
    
    return render(request, 'projects/single-project.html', context)

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    
    if request.method == 'POST':
        data_form = ProjectForm(request.POST, request.FILES)
        if data_form.is_valid():
            project = data_form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')
    
    context = {'form':form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        data_form = ProjectForm(request.POST, request.FILES, instance=project)
        if data_form.is_valid():
            data_form.save()
            return redirect('projects')
    
    context = {'form':form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.objects.get(id=pk)
    
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    
    context = {'object':project}
    
    return render(request, 'projects/delete_template.html', context)