from django.shortcuts import render

# Create your views here.


def welcome_view(request):
    return render(request, 'healthyhoos/welcome.html')


def login_view(request):
    return render(request, 'healthyhoos/login.html')


def home_view(request):
    return render(request, 'healthyhoos/home.html')


def nutrition_view(request):
    return render(request, 'healthyhoos/nutrition.html')


def physical_view(request):
    return render(request, 'healthyhoos/physical.html')


def mental_view(request):
    return render(request, 'healthyhoos/mental.html')


def about_view(request):
    return render(request, 'healthyhoos/about.html')
