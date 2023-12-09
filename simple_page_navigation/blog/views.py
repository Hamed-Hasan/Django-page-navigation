from django.shortcuts import render
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all()
    additional_info = "This is some additional information."
    context = {'blogs': blogs, 'additional_info': additional_info}
    return render(request, 'blog/blog_list.html', context)
