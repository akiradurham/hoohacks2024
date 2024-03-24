from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields you want for your user model
    pass

class Group(models.Model):
    # Fields for the Group model
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_public = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    calendarID = models.CharField(max_length=100)
    
    # Many-to-many field to link Group with CustomUser as admin_users
    admin_users = models.ManyToManyField(CustomUser, related_name='admin_groups')

    # String representation of Group objects
    def __str__(self):
        return self.name

class Task(models.Model):
    # Fields for the Task model
    name = models.CharField(max_length=100)
    category_code = models.CharField(max_length=3)
    time = models.TimeField()
    description = models.TextField()
    
    # Many-to-many field to link Task with CustomUser
    users = models.ManyToManyField(CustomUser, related_name='tasks')

    # String representation of Task objects
    def __str__(self):
        return self.name
