from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.homePage, name = "home-page"),
    path("register-student/", views.registerPageStudent, name="register-page-student"),
    path("register-university/", views.registerPageUniversity, name="register-page-university"),
]
