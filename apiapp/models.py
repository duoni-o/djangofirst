from django.db import models

# apiapp_book이라는 테이블을 생성
class Book(models.Model):
    bid = models.IntegerField(primary_key = True)
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    publisher = models.CharField(max_length = 50)
    publishedDate = models.DateField(max_length = 50)