from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.forumsPageView, name='home'),
    path('forum/<pk>/topics', views.topicsPageView, name="topics"),
]

