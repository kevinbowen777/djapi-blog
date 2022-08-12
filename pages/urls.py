from django.urls import path
from posts.views import PostListView

from .views import AboutPageView, HomePageView


urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    path("posts/", PostListView.as_view(), name="postlist"),
]
