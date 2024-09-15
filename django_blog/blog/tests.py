from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class UserAuthenticationTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_register_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'password123',
            'password2': 'password123',
            'email': 'newuser@example.com'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful registration
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_view(self):
        login = self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)  # Should be able to view profile when logged in

    def test_logout_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Should redirect after logging out

class UserProfileTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

    def test_profile_view(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/profile.html')

    def test_profile_update(self):
        response = self.client.post(reverse('profile'), {
            'username': 'updateduser',
            'email': 'updated@example.com'
        })
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')

class BlogPostTests(TestCase):
    def setUp(self):
        # Create a test user and log them in
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        # Create a blog post
        self.post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post-detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
        self.assertContains(response, self.post.title)

    def test_creat
