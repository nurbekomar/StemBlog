from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from blog.models import *
# Create your views here.

menu = [{'title': "STEM", 'url_name': "home"},
        {'title': "Блог", 'url_name': "blog"},
        {'title': "Автор", 'url_name': "about"},]


def index(request):
    context = {
        'menu': menu,
        'title': 'STEM'
    }
    return render(request, "blog/index.html", context=context)


def blog(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Blog'
    }
    return render(request, "blog/blog.html", context=context)


def about(request):
    return render(request, "blog/about.html", {"menu": menu, "title": "About"})


def show_post(request, post_slug):
    post = get_object_or_404(Blog, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title
    }
    return render(request, "blog/show_post.html", context=context)


def show_category(request, cat_id):
    posts = Blog.objects.filter(cat_id=cat_id)
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Blog'
    }
    return render(request, "blog/blog.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
