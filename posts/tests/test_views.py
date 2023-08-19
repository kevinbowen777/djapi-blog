from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from ..models import Post


class PostTests(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user = get_user_model().objects.create_user(
            username="leopoldbloom",
            email="leopoldbloom@example.com",
            password="secret",
        )

        self.post = Post.objects.create(
            title="A good title",
            body="Nice body content",
            author=self.user,
        )

        self.post2 = Post.objects.create(
            title="A good second title",
            body="Nice body content for a second post",
            author=self.user,
        )

    def test___str__(self):
        assert self.post.__str__() == self.post.title
        assert str(self.post) == self.post.title

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "A good title")
        self.assertEqual(f"{self.post.author}", "leopoldbloom")
        self.assertEqual(f"{self.post.body}", "Nice body content")

    """
    def test_get_absolute_url(self):
        self.assertEqual(
            self.post.get_absolute_url(), f"/posts/{self.post.id}/"
        )
    """

    def test_post_detail_view(self):
        self.client.login(email="leopoldbloom@example.com", password="secret")
        response = self.client.get(f"/api/v1/{self.post.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A good title")

    def test_post_detail_view_failure(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.get(f"/api/v1/{self.post.id}/")
        self.assertEqual(response.status_code, 403)


class PostListViewTest(TestCase):
    def setUp(self):
        url = reverse("post_list")
        self.response = self.client.get(url)

        self.user = get_user_model().objects.create_user(
            username="johndoe",
            email="johndoe@example.com",
            password="secret",
        )

        self.post = Post.objects.create(
            title="A good title",
            body="Nice body content",
            # slug="a-good-title",
            author=self.user,
        )

    def test_view_url_exists_at_desired_location(self):
        # response = self.client.get("/posts/")
        self.assertEqual(self.response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.assertEqual(self.response.status_code, 200)


"""
class SitemapTests(TestCase):
    def setUp(self):
        # url = reverse("sitemap")
        url = "/sitemap.xml"
        self.response = self.client.get(url)

    def test_view_url_exists_at_desired_location(self):
        self.assertEqual(self.response.status_code, 200)


class RSSFeedTests(TestCase):
    def setUp(self):
        url = reverse("post_feed")
        self.response = self.client.get(url)

    def test_feed_url_exists_at_desired_location(self):
        self.assertEqual(self.response.status_code, 200)
"""
