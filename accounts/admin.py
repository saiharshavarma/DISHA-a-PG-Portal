from django.contrib import admin
from .models import Student, University


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user', 'phone')


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user', 'university_name', 'deadline')


admin.site.register(Student, StudentAdmin)
admin.site.register(University, UniversityAdmin)
