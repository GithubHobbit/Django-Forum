from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from . import forms
from django.contrib import messages
from django.contrib.auth import logout


def signup(request):
    if request.method == "GET":
        form = forms.RegistrationForm()
        return render(request, 'accounts/signup.html', {"form": form})

    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('forum:home')
        else:
            return render(request, 'accounts/signup.html', {"form": form})


def logout_view(request):
    logout(request)
    return redirect(reverse('accounts:login'))


# Create your views here.
