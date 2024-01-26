from django.urls import path
from .views import hello, booksAPI, oneBookAPI

urlpatterns = [
    path("hello/", hello),
    path("books/", booksAPI),
    path("book/<int:bid>", oneBookAPI),
]