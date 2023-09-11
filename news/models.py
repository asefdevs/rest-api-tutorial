from django.db import models

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
