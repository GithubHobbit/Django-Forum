from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'forum'
urlpatterns = [
    path('', views.forumsPageView, name='home'),
    path('forum/<pk>/topics', views.topicsPageView, name="topics"),
    path('topic/<pk>/page', views.topicDetailView, name='topic', kwargs={'page': 1}),
    path('topic/<pk>/page/<int:page>', views.topicDetailView, name='topic'),
    path('favorite_topics', views.favoriteMsgDetailView, name='favorite_topics'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




