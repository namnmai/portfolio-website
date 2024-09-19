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
      
	# Define a mapping from technology names to their corresponding Font Awesome icon classes
	tech_icons = {
        'Python': 'fab fa-python',
        'Django': 'fas fa-leaf',  # Using a leaf as a placeholder for Django
        'JavaScript': 'fab fa-js-square',
        'React': 'fab fa-react',
        'HTML5': 'fab fa-html5',
        'CSS3': 'fab fa-css3-alt',
        'Bootstrap': 'fab fa-bootstrap',
        'Git': 'fab fa-git-alt',
        'GitHub': 'fab fa-github',
        'Docker': 'fab fa-docker',
        'AWS': 'fab fa-aws',
        'PostgreSQL': 'fas fa-database',
        'MySQL': 'fas fa-database',
        'Node.js': 'fab fa-node-js',
        'TypeScript': 'fab fa-js-square',
        # Add more technologies as needed
    }

    # Categorize technologies from the model fields
	tech_categories = {
        'Backend': project.backend_technologies.split(',') if project.backend_technologies else [],
        'Frontend': project.frontend_technologies.split(',') if project.frontend_technologies else [],
        'Database': project.database_technologies.split(',') if project.database_technologies else [],
        'Other': project.other_technologies.split(',') if project.other_technologies else []
    }

    # Create a dictionary to store technologies with their respective icons, categorized
	categorized_technologies = {}
	for category, tech_list in tech_categories.items():
		categorized_technologies[category] = []
		for tech in tech_list:
			tech = tech.strip()  # Strip any extra spaces
			icon_class = tech_icons.get(tech, 'fas fa-tools')  # Default icon if not found
			categorized_technologies[category].append({'name': tech, 'icon': icon_class})

	context = {
        'project': project,
        'categorized_technologies': categorized_technologies
    }
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