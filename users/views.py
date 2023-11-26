from rest_framework import generics, status
from rest_framework.response import Response
from users.serializers import CreateUserSerializer
from users.tasks import send_mail_new_user


class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        """Хеширование пароля и отправка письма"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            send_mail_new_user.delay(request.data['email'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
