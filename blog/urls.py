from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # blog main page
    path("/posts", views.posts, name="posts"),
]
