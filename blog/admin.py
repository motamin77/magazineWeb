from django.contrib import admin
from blog.models import POST , CATEGORY

class PostAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    fields=('title','category','author','status','preview','content','publish_date')
    list_display=('id','author','title','status','publish_date','created_date','counted_view')
    list_filter = ('status','publish_date')
    search_fields = ('title','preview','content')
    ordering = ('-created_date',)
    list_per_page = 20
# Register your models here.
admin.site.register(POST,PostAdmin)
admin.site.register(CATEGORY)