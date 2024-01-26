from rest_framework.response import Response
from rest_framework.decorators import api_view

# python에서 @으로 시작하는 단어는 decorator라고 하는데
# 실제 함수를 호출하기 전에 특정 내용을 삽입해서 함수를 실행
# 반복적으로 사용하는 내용이나 직접 작성하기 번거로운 내용을 decorator로 만듦

# GET 요청이 오면 함수를 호출
@api_view(['GET'])
def hello(request):
    return Response("Hello REST API")

from rest_framework import status
from rest_framework.generics import get_object_or_404

# 우리가 만든 거
from .models import Book
from .serializers import BookSerializer

# GET, POST 둘 다 처리하겠다는 뜻
@api_view(['GET', 'POST'])
def booksAPI(request):
    # GET 방식의 처리 - 조회를 요청하는 경우
    if request.method == 'GET':
        # 테이블의 데이터를 전부 가져오기
        books = Book.objects.all()
        # 출력하기 위해서 브라우저의 형식으로 데이터를 변환
        serializer = BookSerializer(books, many = True) # 배열로 만들어줌
        # 출력
        return Response(serializer.data)
    # POST 방식의 처리 - 삽입하는 경우
    elif request.method == "POST":
        # 클라이언트에서 전송된 데이터를 가지고 Model 인스턴스 생성
        serializer = BookSerializer(data = request.data)
        # 유효성 검사를 수행해서 통과하면 삽입하고
        # 그렇지 않으면 실패한 이유를 출력합니다.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
