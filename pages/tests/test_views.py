from django.test import TestCase
from django.urls import resolve, reverse

from ..forms import ContactForm
from ..views import (
    AboutPageView,
    ContactView,
    HomePageView,
    SuccessView,
)


class HomePageTests(TestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_template(self):
        self.assertTemplateUsed(self.response, "pages/home.html")

    def test_home_page_contains_correct_html(self):
        self.assertContains(self.response, "Welcome to the Blog API")

    def test_home_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Not the Homepage")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__,
        )


class AboutPageTests(TestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)

    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_template(self):
        self.assertTemplateUsed(self.response, "pages/about.html")

    def test_about_page_contains_correct_html(self):
        self.assertContains(self.response, "About page")

    def test_about_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Not the About page")

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve("/about/")
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__,
        )


class ContactViewTests(TestCase):
    def setUp(self):
        url = reverse("contact")
        self.response = self.client.get(url)
        self.form_data = {
            "from_email": "joe@example.com",
            "subject": "Test Email",
            "message": "This is a test email",
        }

    def test_contact_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_contact_page_template(self):
        self.assertTemplateUsed(self.response, "pages/contact.html")

    def test_contact_page_contains_correct_html(self):
        self.assertContains(self.response, "Contact Us")

    def test_contact_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Please Go Away")

    def test_contact_page_url_resolves_contactpageview(self):
        view = resolve("/contact/")
        self.assertEqual(
            view.func.__name__,
            ContactView.__name__,
        )

    def test_contact_page_form_is_valid(self):
        form = ContactForm(data=self.form_data)
        self.assertTrue(form.is_valid())


class SuccessViewTests(TestCase):
    def setUp(self):
        url = reverse("success")
        self.response = self.client.get(url)

    def test_success_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_success_page_template(self):
        self.assertTemplateUsed(self.response, "pages/success.html")

    def test_success_page_contains_correct_html(self):
        self.assertContains(
            self.response,
            "Thank you for your message.",
        )

    def test_success_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Please Go Away")

    def test_success_page_url_resolves_success_page_view(self):
        view = resolve("/success/")
        self.assertEqual(
            view.func.__name__,
            SuccessView.__name__,
        )
