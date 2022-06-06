from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.views.generic import ListView
from django.http import HttpResponseRedirect
import student
from member.models import Member
from . import forms
from .forms import ExamCreateForm
from .models import Student, Exam


# Create your views here.
def exam_create(request, pk_exam):
    student = Student.objects.get(pk=pk_exam)
    form = ExamCreateForm(request.POST)
    if request.method == 'POST':
        form = ExamCreateForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = {'exam_author': request.user}
            instance.exam_id = pk_exam

            instance.save()
            return HttpResponseRedirect('/student/student_dashboard?submitted=True')
        else:
            form = ExamCreateForm
            if 'submitted' in request.GET:
                submitted = True
    return render(request, 'student/exam_create.html', {'form': form, 'student': student})


def home(request):
    return render(request=request, template_name="student/home.html")


def student_profile(request):
    return render(request=request, template_name="student/student_profile.html")


def student_dashboard(request):
    students_all = Student.objects.all()
    return render(request, "student/student_dashboard.html", {'students_all': students_all})


def exam_report_view(request):
    exam_results = Exam.objects.all()
    student_exam = Student.objects.all()
    return render(request, "student/exam_report_view.html",
                  {'exam_results': exam_results, 'student_exam': student_exam})
