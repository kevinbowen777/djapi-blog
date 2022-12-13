from accounts.tests.factories import UserFactory
from django.test import TestCase

from .factories import PostFactory


# from ..models import Post


class PostTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.post = PostFactory()

    def test__str__(self):
        assert self.post.__str__() == self.post.title
        assert str(self.post) == self.post.title
