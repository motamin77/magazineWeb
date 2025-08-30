from django import template
from blog.models import POST
from blog.models import CATEGORY

register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts = POST.objects.all()
    return posts

@register.simple_tag(name='posts')
def function():
    posts = POST.objects.all()
    return posts

@register.filter()
def snippet(value, arg):
    return value[:arg] + '...'

@register.inclusion_tag('blog/popularPosts-blog.html')
def popularposts():
    posts = POST.objects.all().order_by('-publish_date')[:5]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-categories.html')
def postCategories():
    posts = POST.objects.filter(status=1)
    categories = CATEGORY.objects.all()
    cat_dict = {}
    for cat in categories:
        cat_dict[cat] = posts.filter(category=cat).count() 
    return {'categories': cat_dict}