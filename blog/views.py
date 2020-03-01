from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def blogs(request):
    count = Blog.objects.count()
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/blogs.html', {'blogs': blogs, 'blogs_count':count})


def details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog': blog})
