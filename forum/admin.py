from django.contrib import admin

from forum.models import Forum, Message, Topic

#  1 Example
@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

#  2 Example
admin.site.register(Topic)
admin.site.register(Message)
