from django.shortcuts import render
from .models import Student


# Create your views here.


def home(request):
    return render(request=request, template_name="student/home.html")


def student_profile(request):
    return render(request=request, template_name="student/student_profile.html")


def student_dashboard(request):
    students_all = Student.objects.all()
    return render(request, "student/student_dashboard.html", {'students_all': students_all})
