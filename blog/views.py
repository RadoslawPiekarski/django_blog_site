from django.shortcuts import render
from django.http import Http404
from .models import Post


# Create your views here.



def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all_posts.html", {
        "all_posts": all_posts
    })


# single post

def post_detail(request, slug):

    # identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post_detail.html", {
        "post": identified_post
    })
