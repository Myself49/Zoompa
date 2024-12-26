from django.db import models
from django.urls import reverse

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=25)
    uni_id = models.CharField( primary_key=True, max_length=10, unique=True)
    email = models.EmailField(unique=True)
    phone_num = models.CharField(max_length=10 ,unique=True)
    address = models.CharField(max_length=30)
    password = models.CharField(max_length=50, unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.name

# Create Forums
class Thread(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("thread_detail", kwargs={"pk": self.pk})

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)