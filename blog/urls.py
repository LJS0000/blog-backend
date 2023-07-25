from django.urls import path
from .views import PostList, PostCreate, PostDetail, CommentList, CommentDetail

app_name = 'blog'

urlpatterns = [
    # 글 목록 조회
    path('posts/', PostList.as_view(), name='posts'),
    # 글 상세 조회
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    # 글 작성, 수정, 삭제
    path('posts/write/', PostCreate.as_view(), name='post-write'),
    # 댓글 조회
    path(
        'posts/<int:pk>/comments/',
        CommentList.as_view(),
        name='comment-list',
    ),
    # 댓글 작성, 수정, 삭제
    path(
        'posts/<int:post_pk>/comments/<int:comment_pk>/',
        CommentDetail.as_view(),
        name='comment-detail',
    ),
    # 좋아요
    # 검색
    # 자기소개
]
