from django.urls import path
from .views import hello_rest_api

app_name = 'blog'

urlpatterns = [
    path('api/hello/', hello_rest_api, name='hello_rest_api'),
    # 글 목록 조회
    # 글 상세 조회
    # 글 작성
    # 글 수정
    # 댓글 작성
    # 댓글 조회
    # 좋아요
    # 검색
    # 자기소개
]
