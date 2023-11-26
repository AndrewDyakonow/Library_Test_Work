from rest_framework import generics
from library.models import Book
from library.serializers import CRUDBookSerializer


class CreateBookAPIView(generics.CreateAPIView):
    """Представление для создания объекта книги"""
    serializer_class = CRUDBookSerializer


class ListBookAPIView(generics.ListAPIView):
    """Представление для отображения списка книг"""
    queryset = Book.objects.all()
    serializer_class = CRUDBookSerializer


class DetailBookAPIView(generics.RetrieveAPIView):
    """Представление для отображения одной книги"""
    queryset = Book.objects.all()
    serializer_class = CRUDBookSerializer
    lookup_field = 'id'


class UpdateBookAPIView(generics.UpdateAPIView):
    """Представление для изменения объекта книги"""
    queryset = Book.objects.all()
    serializer_class = CRUDBookSerializer
    lookup_field = 'id'


class DeleteBookAPIView(generics.DestroyAPIView):
    """Представление для удаления списка книги"""
    queryset = Book.objects.all()
    lookup_field = 'id'
