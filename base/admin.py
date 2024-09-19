from django.contrib import admin

# Register your models here.

from .models import Project, Skill, Tag, Message

class ProjectAdmin(admin.ModelAdmin):
     # Specify what fields should appear in the admin list view
    list_display = ('title', 'created')
    
    # Specify which fields should be searchable in the list view
    search_fields = ('title', 'backend_technologies', 'frontend_technologies', 'database_technologies', 'other_technologies')
    
    # Specify the fields and fieldsets
    fieldsets = (
        (None, {  # General fields section
            'fields': ('title', 'body', 'thumbnail', 'project_url', 'github_url')
        }),
        ('Technologies', {  # Technologies section
            'fields': ('backend_technologies', 'frontend_technologies', 'database_technologies', 'other_technologies'),
        }),
    )

# Register the Project model with the customized ProjectAdmin class
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill)
admin.site.register(Tag)
admin.site.register(Message)
