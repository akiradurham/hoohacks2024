from django.shortcuts import render

# Create your views here.
from .models import Group, Task

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


from django.http import HttpResponse
from django.utils import timezone
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import os.path
import pickle

SCOPES = ['https://www.googleapis.com/auth/calendar']

def welcome_view(request):
    return render(request, 'healthyhoos/welcome.html')


def login_view(request):
    return render(request, 'healthyhoos/login.html')


def home_view(request):
    return render(request, 'healthyhoos/home.html')


def profile_view(request):
    return render(request, 'healthyhoos/profile.html')


@login_required
def nutrition_view(request):
    if request.method == 'POST':
        # If it's a POST request, process the form data
        group_name = request.POST.get('group_name')
        is_admin = request.POST.get('is_admin')
        
        # Convert is_admin to a boolean and set is_public accordingly
        is_public = is_admin == 'on'
        
        # Create a new group
        new_group = Group.objects.create(
            name=group_name,
            description="nutrition",  # Example description
            is_public=is_public
        )

        if is_public:
            new_group.admin_users.add(request.user)
        # Save the new group
        new_group.calendarID = createCalendar(group_name)
        new_group.save()
        
        # Redirect to a different URL after POST
        nutrition_groups = Group.objects.filter(description="nutrition")
        return render(request, 'healthyhoos/nutrition.html', {'nutrition_groups': nutrition_groups})# You might want to redirect to a different URL
        
    else:
        # If it's not a POST request, just render the template with existing groups
        nutrition_groups = Group.objects.filter(description="nutrition")
        return render(request, 'healthyhoos/nutrition.html', {'nutrition_groups': nutrition_groups})


@login_required
def physical_view(request):  
    if request.method == 'POST':
        # If it's a POST request, process the form data
        group_name = request.POST.get('group_name')
        is_admin = request.POST.get('is_admin')
        
        # Convert is_admin to a boolean and set is_public accordingly
        is_public = is_admin == 'on'
        
        # Create a new group
        new_group = Group.objects.create(
            name=group_name,
            description="physical-health",  # Example description
            is_public=is_public
        )

        if is_public:
            new_group.admin_users.add(request.user)
        
        new_group.calendarID = createCalendar(group_name)
        # Save the new group
        new_group.save()
        
        # Redirect to a different URL after POST
        physical_groups = Group.objects.filter(description="physical-health")
        return render(request, 'healthyhoos/physical.html', {'physical_groups': physical_groups})# You might want to redirect to a different URL
        
    else:
        # If it's not a POST request, just render the template with existing groups
        physical_groups = Group.objects.filter(description="physical-health")
        return render(request, 'healthyhoos/physical.html', {'physical_groups': physical_groups})


@login_required
def mental_view(request):  
    if request.method == 'POST':
        # If it's a POST request, process the form data
        group_name = request.POST.get('group_name')
        is_admin = request.POST.get('is_admin')
        
        # Convert is_admin to a boolean and set is_public accordingly
        is_public = is_admin == 'on'
        
        # Create a new group
        new_group = Group.objects.create(
            name=group_name,
            description="mental-health",  # Example description
            is_public=is_public
        )

        if is_public:
            new_group.admin_users.add(request.user)
        
        new_group.calendarID = createCalendar(group_name)
        # Save the new group
        new_group.save()
        
        # Redirect to a different URL after POST
        mental_groups = Group.objects.filter(description="mental-health")
        return render(request, 'healthyhoos/mental.html', {'mental_groups': mental_groups})# You might want to redirect to a different URL
        
    else:
        # If it's not a POST request, just render the template with existing groups
        mental_groups = Group.objects.filter(description="mental-health")
        return render(request, 'healthyhoos/mental.html', {'mental_groups': mental_groups})


def about_view(request):
    return render(request, 'healthyhoos/about.html')


def calendar_view(request):
    return render(request, 'healthyhoos/calendar.html')


@login_required
def nutrition_view_group(request, nutrition_id):
    group = Group.objects.get(id=nutrition_id)
    tasks = group.tasks.all().order_by('id')

    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        task_description = request.POST.get('task_description')
        if task_name and task_description:
            new_task = Task.objects.create(name=task_name, description=task_description, time=timezone.now())
            group.tasks.add(new_task)
            tasks = group.tasks.all().order_by('id')

    return render(request, 'healthyhoos/grouptaskdisplay.html', {'group': group, 'tasks': tasks})


@login_required
def physical_view_group(request, physical_health_id):
    group = Group.objects.get(id=physical_health_id)
    tasks = group.tasks.all().order_by('id')

    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        task_description = request.POST.get('task_description')
        if task_name and task_description:
            new_task = Task.objects.create(name=task_name, description=task_description, time=timezone.now())
            group.tasks.add(new_task)
            tasks = group.tasks.all().order_by('id')

    return render(request, 'healthyhoos/grouptaskdisplay.html', {'group': group, 'tasks': tasks})


@login_required
def mental_view_group(request, mental_health_id):
    group = Group.objects.get(id=mental_health_id)
    tasks = group.tasks.all().order_by('id')

    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        task_description = request.POST.get('task_description')
        if task_name and task_description:
            new_task = Task.objects.create(name=task_name, description=task_description, time=timezone.now())
            group.tasks.add(new_task)
            tasks = group.tasks.all().order_by('id')

    return render(request, 'healthyhoos/grouptaskdisplay.html', {'group': group, 'tasks': tasks})


def createCalendar(name):
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'secret.json', SCOPES)  # Use the downloaded JSON file
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Create a new calendar
    calendar = {
        'summary': name,  # Your new calendar name
        'timeZone': 'America/New_York'  # Your time zone
    }

    created_calendar = service.calendars().insert(body=calendar).execute()
    print('Created Calendar ID: %s' % created_calendar['id'])
    return created_calendar['id']