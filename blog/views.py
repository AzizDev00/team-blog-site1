from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm, BlogForm


# class CategoryListView(View):
#     def get(self, request):
#         return render(request, 'blogs/blog_list.html')

class BlogListView(View):
    template_name = 'blogs/blog_list.html'

    def get(self, request):
        posts = Post.objects.all()
        user = request.user 
        context = {'posts': posts, 'user': user}
        return render(request, self.template_name, context)
    
class BlogDetailView(View):
    def get(self, request, pk):
        blog = get_object_or_404(Post, pk=pk)
        return render(request, 'blogs/blog_detail.html', {'blog': blog})

class BlogCreateView(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blogs/add_blog.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog-list')
        return render(request, 'blogs/add_blog.html', {'form': form})

class BlogUpdateView(View):
    def get(self, request, pk):
        blog = get_object_or_404(Post, pk=pk)
        form = BlogForm(instance=blog)
        return render(request, 'blogs/update_blog.html', {'form': form, 'blog': blog})

    def post(self, request, pk):
        blog = get_object_or_404(Post, pk=pk)
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return render(request, 'blogs/blog_detail.html', {'form': form, 'blog': blog})

        return render(request, 'blogs/update_blog.html', {'form': form, 'blog': blog})

class BlogDeleteView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blogs/delete_blog.html', {'post': post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect(reverse_lazy('blogs:blog-list'))