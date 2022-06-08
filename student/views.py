import datetime

from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect
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
            instance.exam_author = request.user
            instance.student_id = pk_exam
            test_results = (instance.form_cadence,
                            instance.contact,
                            instance.one_step,
                            instance.sparring,
                            instance.ecas,
                            instance.boards)
            if test_results == True:
                results = 'pass'
                instance.results = results
            else:
                results = 'fail'
                instance.results = results
            instance.save()
            return HttpResponseRedirect('/student/student_dashboard')
        else:
            form = ExamCreateForm
    return render(request, 'student/exam_create.html', {'form'       : form,
                                                        'student'    : student,
                                                        'exam_author': request.user})


def home(request):
    return render(request=request, template_name="student/home.html")


def student_profile(request):
    return render(request=request, template_name="student/student_profile.html")


def student_dashboard(request):
    students_all = Student.objects.all()
    return render(request, "student/student_dashboard.html", {'students_all': students_all})


class exam_list(ListView):
    queryset = Exam.objects.filter()
    template_name = "student/exam_list.html"


"""
def exam_report_view(request):
    exam_results = Exam.objects.all()
    student_exam = Student.objects.all()
    print(student_exam)
    print(exam_results)
    return render(request, "student/exam_report_view.html",
                  {'exam_results': exam_results, 'student_exam': student_exam})
"""
