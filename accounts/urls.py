from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout_view, name='logout')
]
