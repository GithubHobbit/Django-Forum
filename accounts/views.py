from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from accounts.models import CustomUser
from django.contrib import messages
from django.contrib.auth import logout

from .forms import ProfileForm, RegistrationForm


def signup(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, 'accounts/signup.html', {"form": form})

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('forum:home')
        else:
            return render(request, 'accounts/signup.html', {"form": form})


def logout_view(request):
    logout(request)
    return redirect(reverse('accounts:login'))

@login_required
def profile_view(request):
    if request.method == 'GET':
        form = ProfileForm(instance=request.user)
        return render(request, 'accounts/profile.html', {'form': form})
        
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('accounts:profile')
        else:
            print('NOT_VALID')
            return render(request, 'accounts/profile.html', {'form': form})
            


# Create your views here.
