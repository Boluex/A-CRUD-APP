from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='post_images',blank=True)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    # liked=models.ManyToManyField(custo,default=None,blank=True)

class comment(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(post,on_delete=models.CASCADE)
    comment=models.CharField(max_length=100)
    image=models.ImageField(upload_to='comment_images',blank=True)
    date_posted=models.DateTimeField(auto_now_add=True)

