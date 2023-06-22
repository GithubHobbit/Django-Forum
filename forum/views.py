from django.db.models import Count, OuterRef, Subquery
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from forum.models import Forum, Message, Topic
from .models import CustomUser

# @login_required
def forumsPageView(request):
    last_msg_subquery = Message.objects.filter(topic__forum__id=OuterRef('pk')).order_by('-creation_date')[:1]
    queryset = Forum.objects \
        .annotate(topic_cnt=Count('topic')) \
        .annotate(msg_cnt=Count('topic__message')) \
        .annotate(last_msg_date=Subquery(last_msg_subquery.values('creation_date'))) \
        .annotate(last_msg_topic=Subquery(last_msg_subquery.values('topic__title'))) \
        .annotate(last_msg_user=Subquery(last_msg_subquery.values('author__username')))

    return render(request, 'forum/forums.html', {"forums": queryset})


def topicsPageView(request, pk):
    last_msg_subquery = Message.objects.filter(topic__id=OuterRef('pk')).order_by('-creation_date')[:1]
    queryset = Topic.objects.filter(forum__id=pk) \
        .annotate(msg_cnt=Count('message')) \
        .annotate(last_msg_date=Subquery(last_msg_subquery.values('creation_date'))) \
        .annotate(last_msg_user=Subquery(last_msg_subquery.values('author__username'))) \
        # .annotate(is_favorite=Topic.objects.filter(customuser__id=request.user.id).)
    return render(request, 'forum/topics.html', {"topics": queryset})
    

def topicDetailView(request, pk, page=1):
    if request.method == "GET":
        topic = Topic.objects.filter(id=pk).get()
        messages = Message.objects.filter(topic__id=pk).order_by('creation_date')[(page-1) * 20 : page * 20]
        return render(request, 'forum/topic_detail.html', {'topic': topic, 'messages': messages})

    if request.method == "POST":
        if request.POST['message']:
            # author = CustomUser.objects.filter(id=request.user.id).get()
            topic = Topic.objects.filter(id=request.POST['topic_id']).get()
            Message.objects.create(text=request.POST['message'], author=request.user, topic=topic)
            messages = Message.objects.filter(topic__id=pk).order_by('creation_date')[(page-1) * 20 : page * 20]
            return render(request, 'forum/topic_detail.html', {'topic': topic, 'messages': messages})

def favoriteMsgDetailView(request):
    topics = Topic.objects.filter(customuser__id=request.user.id)
    return render(request, 'forum/topics.html', {'topics': topics})


# Create your views here.
