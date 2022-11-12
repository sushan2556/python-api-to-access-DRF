from django.contrib import admin
from .models import Student
# Register your models here.
class Studentadmin(admin.ModelAdmin):
    list_display = ['id','name','city']

admin.site.register(Student,Studentadmin)