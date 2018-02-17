from django.contrib import admin

from post.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'contents', 'photo']
    list_display_links = ['id', 'title', 'contents']


