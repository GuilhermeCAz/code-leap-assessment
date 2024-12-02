from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .models import Post


class PostAPITest(TestCase):
    def setUp(self) -> None:
        self.post_data = {
            'username': 'testuser',
            'title': 'Test Post',
            'content': 'This is a test post.',
        }
        self.updated_data = {
            'username': 'testuser',
            'title': 'Updated Title',
            'content': 'Updated content.',
        }
        self.post = Post.objects.create(**self.post_data)

        self.collection_url = reverse('post-collection')
        self.item_url = reverse(
            'post-item',
            kwargs={'pk': self.post.id},
        )

    def test_get_posts_collection(self) -> None:
        response = self.client.get(self.collection_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['title'] == self.post.title

    def test_create_post(self) -> None:
        response = self.client.post(
            self.collection_url,
            {
                'username': 'newuser',
                'title': 'New Post',
                'content': 'This is a new post.',
            },
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert Post.objects.count() == 2  # noqa: PLR2004

    def test_get_single_post(self) -> None:
        response = self.client.get(self.item_url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == self.post.title

    def test_update_post_with_put(self) -> None:
        response = self.client.put(
            self.item_url,
            self.updated_data,
            content_type='application/json',
        )
        assert response.status_code == status.HTTP_200_OK
        self.post.refresh_from_db()
        assert self.post.title == self.updated_data['title']
        assert self.post.content == self.updated_data['content']

    def test_update_post_with_patch(self) -> None:
        response = self.client.patch(
            self.item_url,
            {'title': 'Partially Updated Title'},
            content_type='application/json',
        )
        assert response.status_code == status.HTTP_200_OK
        self.post.refresh_from_db()
        assert self.post.title == 'Partially Updated Title'

    def test_delete_post(self) -> None:
        response = self.client.delete(self.item_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Post.objects.count() == 0
