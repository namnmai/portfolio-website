from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
	title = models.CharField(max_length=200, null=True)
	thumbnail = models.ImageField(null=True)
	body = models.TextField()
	project_url = models.URLField(blank=True, null=True)
	github_url = models.URLField(blank=True, null=True)

	# New fields for categorized technologies
	backend_technologies = models.CharField(max_length=255, blank=True, help_text="Comma-separated list of backend technologies.")
	frontend_technologies = models.CharField(max_length=255, blank=True, help_text="Comma-separated list of frontend technologies.")
	database_technologies = models.CharField(max_length=255, blank=True, help_text="Comma-separated list of database technologies.")
	other_technologies = models.CharField(max_length=255, blank=True, help_text="Comma-separated list of other technologies.")
	
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	def __str__(self):
		return self.title
	
class Skill(models.Model):
	title = models.CharField(max_length=200, null=True)
	body = models.TextField(null=True, blank=True)
	logo = models.ImageField(null=True)
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	def __str__(self):
		return self.title
	

class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	def __str__(self):
		return self.name
	
class Message(models.Model):
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	subject = models.CharField(max_length=200, null=True)
	body = models.TextField()
	is_read = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	def __str__(self):
		return self.name