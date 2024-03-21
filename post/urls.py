from django.urls import path
from .views import PostListView, PostCreateView, PostsView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('', PostCreateView.as_view(), name='post_create'),
    path('post-list/',PostsView.as_view(), name='post_list'),
]
