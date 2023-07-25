from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Post


class PostAPITestCase(APITestCase):
    def test_list_posts(self):
        # User 인스턴스 생성
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user2 = User.objects.create_user(username='testuser2', password='12345')

        # 테스트용 데이터 생성
        Post.objects.create(
            title='Test title 1', content='Test content 1', author=test_user1
        )
        Post.objects.create(
            title='Test title 2', content='Test content 2', author=test_user2
        )

        url = reverse('blog:posts')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
