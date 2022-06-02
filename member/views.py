from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView

from student.models import Student


# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration was successful'))
            return redirect('main:home')
    else:
        form = UserCreationForm()
    return render(request, 'member/authentication/register_user.html', {'form': form})


"""
class StudentListView(ListView):
    model = Exam
    template_name = 'reports.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'exam'
    paginate_by = 5
"""
