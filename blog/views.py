from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from blog.models import *
# Create your views here.

menu = [{'title': "STEM", 'url_name': "home"},
        {'title': "Blog", 'url_name': "blog"},
        {'title': "About", 'url_name': "about"},
        {'title': "Contactoo", 'url_name': "contact"}]


def index(request):
    context = {
        'menu': menu,
        'title': 'STEM'
    }
    return render(request, "blog/index.html", context=context)


def blog(request):
    posts = Blog.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Blog'
    }
    return render(request, "blog/blog.html", context=context)


def about(request):
    return render(request, "blog/about.html", {"menu": menu, "title": "About"})


def contact(request):
    return render(request, "blog/contact.html", {"menu": menu, "title": "Contact0000adasda00000"})


def show_post(request, post_id):
    return render(request, "blog/show_post.html", {"menu": menu, "title": "Posts"})


def show_category(request, cat_id):
    posts = Blog.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Blog'
    }
    return render(request, "blog/blog.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
