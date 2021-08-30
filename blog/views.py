from django.shortcuts import render
from django.http import Http404

# Create your views here.
post = [
{
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpg",
    "author": "Radek",
    "date": date(2021, 09, 29),
    "title" "Mountain Hiking",
    "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec ligula magna. Praesent aliquet rhoncus massa, blandit rhoncus mauris malesuada in.",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec ligula magna. Praesent aliquet rhoncus massa, blandit rhoncus mauris malesuada in. Sed vulputate, orci id varius rutrum, eros nunc mollis nunc, vitae ornare sem orci sed nisi."
},
{
    "slug": "second-post",
    "image": "mountains.jpg",
    "author": "Radek",
    "date": date(2021, 09, 23),
    "title" "Second post",
    "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec ligula magna. Praesent aliquet rhoncus massa, blandit rhoncus mauris malesuada in.",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec ligula magna. Praesent aliquet rhoncus massa, blandit rhoncus mauris malesuada in. Sed vulputate, orci id varius rutrum, eros nunc mollis nunc, vitae ornare sem orci sed nisi."
},
]
def index(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/all_posts.html")


# single post

def post_detail(request, slug):
    return render(request, "blog/post_detail.html")

