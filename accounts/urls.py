from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('register_student', views.registerStudent, name="register_student"),
    path('register_university', views.registerUniversity,
         name="register_university"),
    path('logout', views.logout, name="logout"),
]
