from django.db import models
from django.contrib.auth.models import User


class category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class POST(models.Model):
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    category = models.ManyToManyField(category)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    preview = models.TextField(null=True)
    content = models.TextField()
    status=models.BooleanField(default=True)
    counted_view=models.IntegerField(default=0)
    publish_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['created_date']

    def __str__(self):   
        return self.title