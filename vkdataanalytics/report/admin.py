from django.contrib import admin
from .models import VKUser, Post, Comment


admin.site.register(VKUser)
admin.site.register(Post)
admin.site.register(Comment)
