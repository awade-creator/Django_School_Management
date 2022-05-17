from django.shortcuts import render, redirect

#
from django.core.paginator import Paginator
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.


def home(request):
    return render(request=request, template_name="main/home.html")


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Registration successful.")
            return redirect("login")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            form = NewUserForm
        return render(
            request=request, template_name="main/register.html", context={"form": form}
        )


def logout_request(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    messages.info(request, " Logged Out Successfully!")

    # Take the user back to the homepage.
    return redirect("main/home.html")


def profile(request):
    pass
