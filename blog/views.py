from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import  CreateView , UpdateView , DeleteView
from .models import Post
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Post
    template_name = 'blog.html'

class BlogDetailView(ListView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'description', 'image']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'description', 'image']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog')
