from rest_framework import generics

from library.models import Book
from library.serializers import CRUDBookSerializer


class CreateBookAPIView(generics.CreateAPIView):
    serializer_class = CRUDBookSerializer


class ListBookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = CRUDBookSerializer


class DetailBookAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = CRUDBookSerializer
    lookup_field = 'id'


class UpdateBookAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = CRUDBookSerializer
    lookup_field = 'id'


class DeleteBookAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    lookup_field = 'id'
