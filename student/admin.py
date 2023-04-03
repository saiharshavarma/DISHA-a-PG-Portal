from django.contrib import admin
from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('student', 'university', 'status')


admin.site.register(Application, ApplicationAdmin)
