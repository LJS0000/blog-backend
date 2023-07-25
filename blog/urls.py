from django.urls import path
from .views import PostList, PostDetail

app_name = 'blog'

urlpatterns = [
    # 글 목록 조회
    path('api/blog/posts/', PostList.as_view()),
    # 글 상세 조회
    path('api/blog/posts/<int:pk>/', PostDetail.as_view()),
    # 글 작성
    # 글 수정
    # 댓글 작성
    # 댓글 조회
    # 좋아요
    # 검색
    # 자기소개
]
