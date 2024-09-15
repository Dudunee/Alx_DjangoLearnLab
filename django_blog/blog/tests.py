from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

class BlogTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.user
        )
        self.client.login(username='testuser', password='password')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post-detail', args='1'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_add_comment(self):
        response = self.client.post(reverse('add-comment', args='1'), {'content': 'Test Comment'})
        self.assertEqual(response.status_code, 302)  # redirect after post
        self.assertTrue(Comment.objects.filter(content='Test Comment').exists())

    def test_edit_comment(self):
        comment = Comment.objects.create(post=self.post, author=self.user, content='Original Comment')
        response = self.client.post(reverse('edit-comment', args=[1, comment.id]), {'content': 'Updated Comment'})
        self.assertEqual(response.status_code, 302)  # redirect after post
        comment.refresh_from_db()
        self.assertEqual(comment.content, 'Updated Comment')

    def test_delete_comment(self):
        comment = Comment.objects.create(post=self.post, author=self.user, content='Comment to delete')
        response = self.client.post(reverse('delete-comment', args=[1, comment.id]))
        self.assertEqual(response.status_code, 302)  # redirect after delete
        self.assertFalse(Comment.objects.filter(id=comment.id).exists())
