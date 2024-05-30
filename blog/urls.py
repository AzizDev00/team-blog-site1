from django.urls import path
from .views import BlogListView, BlogDetailView , BlogCreateView, BlogUpdateView , BlogDeleteView


urlpatterns = [
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='post_delete'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='post_update'),
    path('post/create/', BlogCreateView.as_view(), name='post_create'),
    path('', BlogListView.as_view(), name='blog'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]