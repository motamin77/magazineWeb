from django.contrib import admin
from django.urls import path
from blog.views import *

app_name= 'blog'

urlpatterns = [
    path('', blog_page, name= 'index'),
    path('single', blog_single, name= 'single'), 

]
