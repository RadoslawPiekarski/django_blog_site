from django.shortcuts import render
from django.http import Http404
from datetime import date

# Create your views here.

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Radek",
        "date": date(2021, 8, 29),
        "title": "Mountain Hiking",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec ligula magna. Praesent aliquet rhoncus massa, blandit rhoncus mauris malesuada in.",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec ligula magna. Praesent aliquet rhoncus massa, blandit rhoncus mauris malesuada in. Sed vulputate, orci id varius rutrum, eros nunc mollis nunc, vitae ornare sem orci sed nisi."
    },
    {
        "slug": "second-post",
        "image": "mountains.jpg",
        "author": "Radek",
        "date": date(2021, 8, 23),
        "title": "Second post",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec ligula magna. Praesent aliquet rhoncus massa, blandit rhoncus mauris malesuada in.",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec ligula magna. Praesent aliquet rhoncus massa, blandit rhoncus mauris malesuada in. Sed vulputate, orci id varius rutrum, eros nunc mollis nunc, vitae ornare sem orci sed nisi."
    },
]

def get_date(post):
    return post['date']


def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all_posts.html")


# single post

def post_detail(request, slug):
    return render(request, "blog/post_detail.html")

