from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView

from exam.forms import ExamCreateForm, RawExamCreateForm
from exam.models import Exam
from student.models import Student


# Create your views here.
def home(request):
    return render(request, "exam/home.html")


def exam_create(request, pk=None):
    instance = get_object_or_404(Student, id=pk)
    e_form = RawExamCreateForm()
    if request.method == 'POST':
        e_form = RawExamCreateForm(request.POST)
        if e_form.is_valid():
            print(e_form.cleaned_data)
            Exam.objects.create(**e_form.cleaned_data)
        else:
            print(e_form.errors)

    context = {
        'First Name'  : instance.first_name,
        'Last Name'   : instance.last_name,
        'Current Rank': instance.rank,
        'instance'    : instance,
        'e_form'      : e_form,
    }
    return render(request, 'exam/exam_create.html', context)


def exam_detail_view(request):
    return render(request, "exam/exam_detail_view.html")


# charts.js for exam result reporting
def pie_chart(request):
    pass
