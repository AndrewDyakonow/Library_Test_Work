from rest_framework.serializers import ModelSerializer

from library.models import Book


class CRUDBookSerializer(ModelSerializer):
    """Сериализатор объектов книг"""
    class Meta:
        model = Book
        fields = '__all__'
