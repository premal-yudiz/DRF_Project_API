from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    # index = serializers.SerializerMethodField()

    class Meta:
        model = Author
        # exclude = ['id']
        fields = '__all__'

        
class BookSerializer(serializers.ModelSerializer):
    book_author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        author_data = validated_data.pop('book_author')
        author = Author.objects.create(**author_data)
        book = Book.objects.create(book_author=author, **validated_data)
        return book
