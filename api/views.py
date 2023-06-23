from django.shortcuts import render
from rest_framework.response import Response
from .models import Author,Book
from .serializers import AuthorSerializer,BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.filters import SearchFilter,OrderingFilter


# class Author_List_Create(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

 


class AuthorModelViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions] #not read without authenticate
    filter_backends = [OrderingFilter,SearchFilter]
    search_fields = ['author_name']
    ordering_fields = ['author_name']



class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions] #not read without authenticate
    filter_backends = [SearchFilter]
    search_fields = ['book_name']
    # ordering_field = '__all__'


