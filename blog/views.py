from django.shortcuts import render
from .models import Blog

# Create your views here.
def blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/blogs.html', {'blogs': blogs})
