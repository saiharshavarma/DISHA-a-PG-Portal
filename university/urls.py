from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="university_home"),
    path('profile', views.profile, name="university_profile"),
    path('status/<application>', views.changeStatus, name="change_status"),
]
