from django.shortcuts import render , get_object_or_404
from blog.models import POST

def blog_page(request):
    posts = POST.objects.all()
    context={'posts':posts}
    return render(request, 'blog/blog.html',context)

def blog_single(request,pid):
    posts = POST.objects.all()
    post = get_object_or_404(posts,pk=pid)
    context={'post':post}
    return render(request, 'blog/blog-details.html',context)
