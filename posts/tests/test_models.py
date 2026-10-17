from django.test import TestCase

from accounts.tests.factories import UserFactory

from .factories import PostFactory

# from ..models import Post


class PostTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.post = PostFactory()

    def test__str__(self):
        assert str(self.post) == self.post.title
