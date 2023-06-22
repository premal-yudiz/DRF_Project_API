from django.contrib import admin
from .models import Author,Book

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','author_name','author_email']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','book_name','book_author','book_description','book_price']