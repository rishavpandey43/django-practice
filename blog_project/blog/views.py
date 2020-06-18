from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Rishav Pandey',
        'title': 'Blog Post',
        'content': 'First post content',
        'date_posted': 'June 18, 2020'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post',
        'content': 'Second post content',
        'date_posted': 'June 19, 2020'
    }
]


def home(request):
    context = {
        'posts': posts,
        'title': "Home"
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {'title': "About"})
