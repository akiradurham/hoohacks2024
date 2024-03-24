from django.shortcuts import render

# Create your views here.
from .models import Group

from django.shortcuts import redirect




def welcome_view(request):
    return render(request, 'healthyhoos/welcome.html')


def login_view(request):
    return render(request, 'healthyhoos/login.html')


def home_view(request):
    return render(request, 'healthyhoos/home.html')




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
        
        # Save the new group
        new_group.save()
        
        # Redirect to a different URL after POST
        nutrition_groups = Group.objects.filter(description="nutrition")
        return render(request, 'healthyhoos/nutrition.html', {'nutrition_groups': nutrition_groups})# You might want to redirect to a different URL
        
    else:
        # If it's not a POST request, just render the template with existing groups
        nutrition_groups = Group.objects.filter(description="nutrition")
        return render(request, 'healthyhoos/nutrition.html', {'nutrition_groups': nutrition_groups})





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
        
        # Save the new group
        new_group.save()
        
        # Redirect to a different URL after POST
        physical_groups = Group.objects.filter(description="physical-health")
        return render(request, 'healthyhoos/physical.html', {'physical_groups': physical_groups})# You might want to redirect to a different URL
        
    else:
        # If it's not a POST request, just render the template with existing groups
        physical_groups = Group.objects.filter(description="physical-health")
        return render(request, 'healthyhoos/physical.html', {'physical_groups': physical_groups})



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
