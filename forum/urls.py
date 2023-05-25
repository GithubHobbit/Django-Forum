from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'forum'
urlpatterns = [
    # path('', login_required(views.HomePageView.as_view()), name='home'),
    path('', views.homePageView, name='home'),
]

