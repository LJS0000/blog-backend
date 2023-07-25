from django.urls import path
from .views import PostList, PostDetail

app_name = 'blog'

urlpatterns = [
    # 글 목록 조회
    path('posts/', PostList.as_view(), name='posts'),
    # 글 상세 조회
    path('posts/<int:pk>/', PostDetail.as_view(), name='detail'),
    # 글 작성
    # 글 수정
    # 댓글 작성
    # 댓글 조회
    # 좋아요
    # 검색
    # 자기소개
]
