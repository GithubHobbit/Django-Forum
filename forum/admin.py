from django.contrib import admin

from forum.models import Forum, Message, Topic

admin.site.register(Forum)
admin.site.register(Topic)
admin.site.register(Message)

# Register your models here.
