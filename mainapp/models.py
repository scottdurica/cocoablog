from django.db import models
from django.utils import timezone



class Author(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    species = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    


