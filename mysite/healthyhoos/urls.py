from . import views

from django.urls import path


app_name = "healthyhoos"
urlpatterns = [
    path("", views.indexview, name="index"),
]