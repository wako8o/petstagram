from django.contrib import admin

from petstagram.common.models import Comment, Like


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
