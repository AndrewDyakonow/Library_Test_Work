from rest_framework.serializers import ModelSerializer

from library.models import Book


class CRUDBookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
