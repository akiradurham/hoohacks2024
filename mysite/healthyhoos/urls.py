from . import views

from django.urls import path, include
from django.contrib.auth.views import LogoutView


app_name = "healthyhoos"
urlpatterns = [
    path("", views.welcome_view, name="index"),
    path("login/", views.login_view, name="login"),
    path("home/", views.home_view, name="home"),
    path("nutrition/", views.nutrition_view, name="nutrition"),
    path("physical-health/", views.physical_view, name="physical-health"), 
    path("nutrition/<int:nutrition_id>/", views.nutrition_view_group, name="nutrition_group"),
    path("physical-health/<int:physical_health_id>/", views.physical_view_group, name="physical-health_group"),
    path("mental-health/", views.mental_view, name="mental-health"),
    path("mental-health/<int:mental_health_id>/", views.mental_view_group, name="mental-health_group"),
  
    path("about/", views.about_view, name="about"),
    path("profile/", views.profile_view, name="profile"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/', include('allauth.urls')),
]
