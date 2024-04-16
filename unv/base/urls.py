from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name = "home-page"),
    path("register-student/", views.registerPageStudent, name="register-page-student"),
    path("register-university/", views.registerPageUniversity, name="register-page-university"),
    path("student-page", views.studentPage, name = "student-page"),
    path("university-page", views.universityPage, name = "university-page"),
    path("university-page-tap2", views.universityPagTap2, name = "university-page-tap2"),
    path("university-page-gallery", views.universityPageGallery, name = "university-page-gallery"),
    path("university-main-page", views.universityMainPage, name = "university-main-page"),
    path("university-more-info", views.universityMoreInfo, name = "university-more-info"),
    path("university-get-info/<str:image_filename>/", views.universityGetInfoPage, name = "university-get-info"),
    path("logout", views.logoutView.as_view(), name = "log-out")
]
