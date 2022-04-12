from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, "index.html")


@login_required()
def properties(request):
    return render(request, "properties.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def dashboardView(request):
    return render(request, 'dashboard.html')


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, '../templates/registration/register.html', {'form': form})
