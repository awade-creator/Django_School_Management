from django.shortcuts import render, redirect


# Create your views here.


def home(request):
    return render(request=request, template_name="main/home.html")


def profile(request):
    pass
