from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="student_home"),
    path('profile', views.profile, name="student_profile"),
    path('apply/<university>', views.application, name="apply"),
]
