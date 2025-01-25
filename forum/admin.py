from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(UserPost)
admin.site.register(EventUser)
admin.site.register(Answer)
admin.site.register(TopicView)
admin.site.register(BlogPost)
admin.site.register(Event)
admin.site.register(EventGroup)