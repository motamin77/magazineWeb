from django.shortcuts import render , get_object_or_404
from blog.models import POST

def blog_page(request, **kwargs):
    posts = POST.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])

    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])

    context={'posts':posts}
    return render(request, 'blog/blog.html',context)

def blog_single(request,pid):
    posts = POST.objects.filter(status=1)
    post = get_object_or_404(posts,pk=pid)
    context={'post':post}
    return render(request, 'blog/blog-details.html',context)

def test(request):
    posts = POST.objects.all()
    context={'posts':posts}
    return render(request, 'blog/test.html',context)

def blog_category(request, cat_name):
    posts = POST.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context={'posts':posts}
    return render(request, 'blog/blog.html',context)

def blog_search(request):
    posts = POST.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context={'posts':posts}        
    return render(request, 'blog/blog.html',context)
