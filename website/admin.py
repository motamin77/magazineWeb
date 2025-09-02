from django.contrib import admin
from website.models import contact , newsletter

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    list_per_page = 20
       
register = admin.site.register(contact,ContactAdmin)
register = admin.site.register(newsletter)