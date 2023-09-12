from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Journalist(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Article(models.Model):
    author = models.ForeignKey(Journalist, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    text_body = models.TextField()
    city = models.CharField(max_length=120)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    city=models.CharField(max_length=255,null=True, blank=True)
    image=models.ImageField(upload_to='profile_photos',null=True, blank=True)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.image:
            img=Image.open(self.image.path)
            if img.height > 600 or img.width > 600:
                output_size=(600,600)
                img.thumbnail(output_size)
                img.save(self.image.path)
                
    def __str__(self):
        return self.user.username
    

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    text=models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username
    
