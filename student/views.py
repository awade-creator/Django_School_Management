from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
import student
from . import forms
from .forms import ExamCreateForm
from .models import Student, Exam


# Create your views here.
def exam_create(request, pk_exam):
    submitted = False
    form = ExamCreateForm
    student = Student.objects.get(id=pk_exam)
    if request.method == 'POST':
        form = ExamCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/student/student_dashboard?submitted=True')
        else:
            form = ExamCreateForm
            if 'submitted' in request.GET:
                submitted = True
    return render(request, 'student/exam_create.html', {'form': form, 'submitted': submitted, 'student': student})


def home(request):
    return render(request=request, template_name="student/home.html")


def student_profile(request):
    return render(request=request, template_name="student/student_profile.html")


def student_dashboard(request):
    students_all = Student.objects.all()
    return render(request, "student/student_dashboard.html", {'students_all': students_all})


def exam_report(request):
    results = Exam.objects.all()
    return render(request, "student/exam_report.html", {'result': results})
