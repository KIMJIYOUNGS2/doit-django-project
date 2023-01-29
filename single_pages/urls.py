from . import views
from django.contrib import admin
from django.urls import path, include

# 도메인 뒤에 about_me/가 붙어있으면 자기소개 페이지
# 도메인 뒤에 아무 것도 없으면 landing() 함수를 실행하여 대문 페이지
# blog 앱과 달리 데이터베이스 연결 필요 없고 단순 html 페이지만 보여주면 됨
urlpatterns = [
    path('about_me/', views.about_me),
    path('', views.landing),
]
