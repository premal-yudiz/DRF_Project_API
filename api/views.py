from django.shortcuts import render
from rest_framework.response import Response
from .models import Author,Book
from .serializers import AuthorSerializer,BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import DjangoModelPermissions

# class Author_List_Create(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

 


class AuthorModelViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions] #not read without authenticate


class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]  
    permission_classes = [DjangoModelPermissions] #not read without authenticate

