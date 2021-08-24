from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="starting_page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:post>", views.post, name="post-page"),
]
