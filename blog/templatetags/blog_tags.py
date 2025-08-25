from django import template
from blog.models import POST

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