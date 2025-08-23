from django.contrib import admin
from blog.models import POST

class PostAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    fields=('title','preview','content','publish_date')
    list_display=('title','publish_date','created_date','counted_view')
    list_filter = ('status','publish_date')
    search_fields = ('title','preview','content')
    ordering = ('-created_date',)
    list_per_page = 20
# Register your models here.
admin.site.register(POST,PostAdmin)