from django.contrib import admin
from .models import Student, Exam


# Register your models here.

class Students(admin.ModelAdmin):
    admin.site.register(Student)
    admin.site.register(Exam)
