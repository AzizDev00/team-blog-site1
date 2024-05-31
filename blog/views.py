from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Post ,  Category
from django.urls import reverse_lazy


class CategoriesListView(View):
    def get(self, request):
        category = Category.objects.all()

        return render(request, 'categories.html', {'categorys': category})

class BlogListView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog.html', {'posts': posts})

class BlogDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'post_detail.html', {'post': post})

class BlogCreateView(View):
    def get(self, request):
        return render(request, 'post_create.html')

    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        post = Post(title=title, description=description, image=image)
        post.save()
        return redirect('blog')

class BlogUpdateView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'post_update.html', {'post': post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.title = request.POST.get('title')
        post.description = request.POST.get('description')
        if request.FILES.get('image'):
            post.image = request.FILES.get('image')
        post.save()
        return redirect('post_detail', pk=post.pk)

class BlogDeleteView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'post_delete.html', {'post': post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect(reverse_lazy('blog'))
