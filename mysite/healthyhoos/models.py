from django.db import models

# User model
class User(models.Model):
    # Assuming the 'name' field is unique to each user.
    name = models.CharField(max_length=100)
    # Groups is a many-to-many field because a user can belong to multiple groups.
    groups = models.ManyToManyField('Group', related_name='users')

# Group model
class Group(models.Model):
    # Name of the group.
    name = models.CharField(max_length=100)
    # Description of the task. 
    description = models.TextField() 
    is_public = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    # calendar id
    calendarID = models.CharField(max_length=100)
    # Tasks is a many-to-many field assuming a group can have multiple tasks.
    tasks = models.ManyToManyField('Task', related_name='groups')
    admin_users = models.ManyToManyField(User, related_name='admin_groups')

# Task model
class Task(models.Model):
    # Name of the task, under a category that can have maximum of 3 characters.
    name = models.CharField(max_length=100)
    # The category code seems to be a fixed-length field, hence CharField with max_length=3.
    category_code = models.CharField(max_length=3)
    # Time could mean either duration or a specific time; assuming it's a time field here.
    time = models.TimeField()
    # Description of the task.
    description = models.TextField()
    # Users is a many-to-many field as a task can be assigned to multiple users.
    users = models.ManyToManyField(User, related_name='tasks')