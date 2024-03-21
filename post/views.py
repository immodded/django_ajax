from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views import View
from .models import Post
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.core.paginator import Paginator
class PostCreateView(CreateView):
    model = Post
    template_name = "form.html"
    fields = "__all__"
    success_url = reverse_lazy("post_create")

class PostListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required.'}, status=401)
        
        posts = Post.objects.all()

        # Pagination
        paginator = Paginator(posts, 1)  # Show 10 posts per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Filtering (if any)
        # Example: You can do filtering by URL query parameters
        # For example, if you want to filter posts by its title:
        # title_filter = request.GET.get('title')
        # if title_filter:
        #     posts = posts.filter(title__icontains=title_filter)

        data = {
            'posts': [{'title': post.title} for post in page_obj],
            'has_next': page_obj.has_next(),
            'has_previous': page_obj.has_previous(),
            'page_number': page_obj.number,
            'total_pages': paginator.num_pages
        }
        return JsonResponse(data)


class PostsView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        return render(request, 'post-list.html')