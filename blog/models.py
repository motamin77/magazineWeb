from django.db import models

class POST(models.Model):
    title = models.CharField(max_length=255)
    preview = models.TextField(null=True)
    content = models.TextField()
    status=models.BooleanField(default=False)
    counted_view=models.IntegerField(default=0)
    publish_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['created_date']

    def __str__(self):   
        return self.title