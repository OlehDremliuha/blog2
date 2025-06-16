from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment, Profile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.timezone import now


class ModelTests(TestCase):
    def setUp(self):
        # Создание пользователя
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Создание профиля (можно сделать авто-создание через сигнал)
        self.profile = Profile.objects.create(userId=self.user, bio="Test bio")

        # Заглушка для картинки
        self.image = SimpleUploadedFile(name='test.jpg', content=b'', content_type='image/jpeg')

        # Создание поста
        self.post = Post.objects.create(
            userId=self.user,
            image=self.image,
            title="Test title",
            text="Test content"
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test title")
        self.assertEqual(self.post.userId.username, "testuser")

    def test_comment_creation(self):
        comment = Comment.objects.create(
            userId=self.user,
            postId=self.post,
            text="Nice post!",
            date=now()
        )
        self.assertEqual(comment.text, "Nice post!")
        self.assertEqual(comment.userId.username, "testuser")

    def test_profile_str_method(self):
        self.assertEqual(str(self.profile), "testuser")