from django.urls import path
from library.apps import LibraryConfig
from library.views import (CreateBookAPIView,
                           ListBookAPIView,
                           DetailBookAPIView,
                           UpdateBookAPIView,
                           DeleteBookAPIView)

app_name = LibraryConfig.name

urlpatterns = [
    path('create/', CreateBookAPIView.as_view(), name='create_book'),
    path('list/', ListBookAPIView.as_view(), name='create_book'),
    path('detail/<int:id>/', DetailBookAPIView.as_view(), name='create_book'),
    path('update/<int:id>/', UpdateBookAPIView.as_view(), name='create_book'),
    path('delete/<int:id>/', DeleteBookAPIView.as_view(), name='create_book'),
]
