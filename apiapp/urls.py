from django.urls import path
from .views import hello, booksAPI

urlpatterns = [
    path("hello/", hello),
    path("books/", booksAPI),
]