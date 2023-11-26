from rest_framework import serializers
from users.models import Users


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'

