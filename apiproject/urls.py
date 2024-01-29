from django.contrib import admin
from django.urls import path
# url의 처리를 다른 모듈에게 위임하고자 할 때 사용하는 패키지를 import
from django.urls import include

from apiapp import views

# path("example/", include("apiapp.urls")), 문장은
# example로 시작하는 요청이 오면 apiapp 애플리케이션의 urls.py 파일에 처리를 위임
urlpatterns = [
    path('admin/', admin.site.urls),
    path('example/', include("apiapp.urls")),
    path('ajax/', views.ajax)
]
# ajax/ 라는 요청이 왔을 떄 apiapp.views 파일의 ajax 함수가 처리하도록 설정
