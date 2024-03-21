from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views import View
from .models import Post
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

class PostCreateView(CreateView):
    model = Post
    template_name = "form.html"
    fields = "__all__"
    success_url = reverse_lazy("post_create")

class PostListView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  
            return JsonResponse({'error': 'Authentication required.'}, status=404)
        
        posts = Post.objects.all()
        data = {'posts': [{'title': post.title} for post in posts]}
        return JsonResponse(data)

class PostsView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        return render(request, 'post-list.html')