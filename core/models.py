from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model): 
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()

    def __str__(self):
        return f" {self.user} "
    
    
    
class Post(models.Model): 
    user =models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")
    title = models.CharField(max_length=200)
    description  = models.CharField(max_length=500)
    image = models.ImageField(upload_to='img')
    def __str__(self):
        return f" {self.title} "


    
    
    
# class Comment(models.Model): 
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     post = models.ForeignKey(Post,on_delete=models.CASCADE)
#     context = models.CharField(max_length=2000)
#     reply = models.ForeignKey('self',on_delete=models.CASCADE)
    
    
    
    
    
    
class Photos(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img')