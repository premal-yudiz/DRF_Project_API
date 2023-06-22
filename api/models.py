
from django.db import models

# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=50)
    author_email = models.EmailField()
    author_profile_pic = models.ImageField()

    def __str__(self):
        return self.author_name


class Book(models.Model):
    book_name = models.CharField(max_length=50)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='author')
    book_description = models.TextField()
    book_price = models.IntegerField()
    book_img = models.ImageField()


    def __str__(self):
        return self.book_name
