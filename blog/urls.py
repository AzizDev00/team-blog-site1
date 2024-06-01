
from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = 'blogs'

urlpatterns = [
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog-delete'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog-update'),
    path('post/create/', BlogCreateView.as_view(), name='blog-create'),
    path('', BlogListView.as_view(), name='blog-list'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
]