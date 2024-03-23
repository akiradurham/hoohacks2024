from . import views

from django.urls import path


app_name = "healthyhoos"
urlpatterns = [
    path("", views.welcome_view, name="index"),
    path("home/", views.home_view, name="home"),
    path("nutrition/", views.nutrition_view, name="nutrition"),
    path("physical-health/", views.physical_view, name="physical-health"),
    path("mental-health/", views.mental_view, name="mental-health"),
    path("about/", views.about_view, name="about"),
]
