from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=20)


class Tag(models.Model):
    caption = models.CharField(max_length=15)


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    excerpt = models.CharField(max_length=256)
    image_name = models.CharField(max_length=20)
    date = models.DateField
    slug = models.SlugField
    content = models.TextField
    tag = models.ManyToManyField(Tag)
