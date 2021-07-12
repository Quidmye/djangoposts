from django.contrib import admin
from posts.models import PostModel

# Register your models here.
@admin.register(PostModel)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'author', 'content')

