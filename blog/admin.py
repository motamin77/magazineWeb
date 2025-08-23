from django.contrib import admin
from blog.models import POST

class PostAdmin(admin.ModelAdmin):
    list_display=('title','content','created_date')
# Register your models here.
admin.site.register(POST,PostAdmin)