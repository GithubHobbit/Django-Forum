from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# @login_required
def homePageView(request):
    return render(request, 'forum/home.html')


# Create your views here.
