from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Posts, Category
from django.core.cache import cache
from django.utils.cache import get_cache_key
from django.views.generic import ListView


# Create your views here.
def index(request):
    context = {
        'title': 'Домашняя страница',
    }
    return render(request, 'main/index.html', context)


class PostsListView(ListView):
    model = Posts
    template_name = 'main/posts.html'
    context_object_name = 'posts'


class PostsDetailView(DetailView):
    model = Posts
    template_name = 'main/posts_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.get_object()
        check = get_object_or_404(Posts, pk=self.kwargs.get('pk'))

        return context


class PostsByCategoryView(ListView):
    template_name = 'posts_by_category.html'
    context_object_name = 'posts'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        cache_key = f'posts_by_category_{category_id}'
        posts = cache.get(cache_key)
        if not posts:
            posts = Posts.objects.filter(category_id=category_id)
            cache.set(cache_key, posts, timeout=60 * 15)  # Кэшируем на 15 минут
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(id=self.kwargs.get('category_id'))
        return context