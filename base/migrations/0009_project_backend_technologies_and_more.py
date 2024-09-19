# Generated by Django 5.1.1 on 2024-09-19 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_project_slug_project_github_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='backend_technologies',
            field=models.CharField(blank=True, help_text='Comma-separated list of backend technologies.', max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='database_technologies',
            field=models.CharField(blank=True, help_text='Comma-separated list of database technologies.', max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='frontend_technologies',
            field=models.CharField(blank=True, help_text='Comma-separated list of frontend technologies.', max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='other_technologies',
            field=models.CharField(blank=True, help_text='Comma-separated list of other technologies.', max_length=255),
        ),
    ]
