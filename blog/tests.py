from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Post


class PostAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpassword')

    def test_list_posts(self):
        # User 인스턴스 생성

        # 테스트용 데이터 생성
        Post.objects.create(
            title='Test title 1', content='Test content 1', author=self.user
        )

        url = reverse('blog:posts')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_post(self):
        url = reverse('blog:post-write')
        data = {'title': 'Title 1', 'content': 'Content 1', 'author': self.user.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_post(self):
        post = Post.objects.create(
            title='Test title 1', content='Test content 1', author=self.user
        )
        url = reverse('blog:post-detail', kwargs={'pk': post.id})
        data = {
            'title': 'Updated title',
            'content': 'Updated content',
            'author': self.user.id,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated title')
        self.assertEqual(response.data['content'], 'Updated content')
