from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from django.views.decorators.cache import cache_page
from .views import PostsListView, PostsByCategoryView

urlpatterns = [
    path('', views.index, name='home'),
    path('posts', cache_page(60)(PostsListView.as_view()), name='posts'),
    path('posts_detail/<int:pk>/', views.PostsDetailView.as_view(), name='posts_detail'),
    path('posts/category/<int:category_id>/', PostsByCategoryView.as_view(), name='posts_by_category'),
]
