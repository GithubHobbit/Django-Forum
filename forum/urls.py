from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.homePageView, name='home'),
]

