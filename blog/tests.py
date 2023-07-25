from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Post, Comment


class PostAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpassword')

    def test_list_posts(self):
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

    def test_delete_post(self):
        post = Post.objects.create(
            title='Test title 1', content='Test content 1', author=self.user
        )
        url = reverse('blog:post-detail', kwargs={'pk': post.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Post.objects.filter(id=post.id).exists())


class CommentAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.post = Post.objects.create(
            title='Test title 1', content='Test content 1', author=self.user
        )
        self.comment = Comment.objects.create(
            content='Test comment 1', author=self.user, post=self.post
        )

    def test_list_comments(self):
        url = reverse('blog:comment-list', kwargs={'pk': self.post.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_comment(self):
        url = reverse('blog:comment-list', kwargs={'pk': self.post.id})
        data = {'content': 'Comment 2', 'author': self.user.id, 'post': self.post.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_comment(self):
        url = reverse(
            'blog:comment-detail',
            kwargs={'post_pk': self.post.id, 'comment_pk': self.comment.id},
        )
        data = {
            'content': 'Updated comment',
            'author': self.user.id,
            'post': self.post.id,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], 'Updated comment')

    def test_delete_comment(self):
        url = reverse(
            'blog:comment-detail',
            kwargs={'post_pk': self.post.id, 'comment_pk': self.comment.id},
        )
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
