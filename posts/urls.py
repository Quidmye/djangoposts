from django.urls import path
from posts.views import PostsViewDeleteUpdate, PostsViewCreate

urlpatterns = [
    path('', PostsViewCreate.as_view(), name='posts_list_create'),
    path('<int:pk>', PostsViewDeleteUpdate.as_view(), name='posts_view_delete_update')
]
