from django.shortcuts import render
from .models import Project, Skill
# Create your views here.

def homePage(request):
	projects = Project.objects.all()
	detailed_skills = Skill.objects.exclude(body='')

	skills = Skill.objects.filter(body='')

	context = {'projects': projects, 'skills': skills, 'detailed_skills': detailed_skills}
	return render(request, 'base/home.html', context)

def projectPage(request, pk):
	project = Project.objects.get(id=pk)
	context = {'project': project}
	return render(request, 'base/project.html', context)