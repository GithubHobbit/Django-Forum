from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
