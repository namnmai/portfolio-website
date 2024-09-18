from django.shortcuts import render, redirect
from .models import Project, Skill, Message
from .forms import MessageForm
from django.contrib import messages
# Create your views here.

def homePage(request):
	projects = Project.objects.all()
	detailed_skills = Skill.objects.exclude(body='')

	skills = Skill.objects.filter(body='')

	form = MessageForm()

	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your message was successfully sent!')

	context = {'projects': projects, 'skills': skills, 'detailed_skills': detailed_skills, 'form' : form}
	return render(request, 'base/home.html', context)


def contactPage(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was successfully sent!')
            return redirect('contact_success')  # Redirect to success page
    else:
        form = MessageForm()
    
    context = {'form': form}
    return render(request, 'base/contact.html', context)


def contactSuccess(request):
    return render(request, 'base/contact_success.html')


def projectPage(request, pk):
	project = Project.objects.get(id=pk)
	context = {'project': project}
	return render(request, 'base/project.html', context)


def inboxPage(request):
	inbox = Message.objects.all().order_by('is_read')

	unread_count = Message.objects.filter(is_read=False).count()

	context = {'inbox': inbox, 'unread_count': unread_count}
	return render(request, 'base/inbox.html', context)


def messagePage(request, pk):
	message = Message.objects.get(id=pk)
	message.is_read = True
	message.save()
	context = {'message': message}
	return render(request, 'base/message.html', context)