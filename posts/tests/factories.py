import datetime  # noqa:F401

import factory
import factory.fuzzy
import pytest

from accounts.tests.factories import UserFactory

from ..models import Post


@pytest.fixture
def post():
    return PostFactory()


class PostFactory(factory.django.DjangoModelFactory):
    author = factory.SubFactory(UserFactory)
    title = factory.fuzzy.FuzzyText(length=12, prefix="Breaking News: ")
    body = factory.fuzzy.FuzzyText(length=50)
    # date = factory.fuzzy.FuzzyDate(datetime.date(2022, 6, 23))

    class Meta:
        model = Post
