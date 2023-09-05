from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from blog.models import *
# Create your views here.

menu = [{'title': "STEM", 'url_name': "home"},
        {'title': "Blog", 'url_name': "blog"},
        {'title': "ABOUT", 'url_name': "about"},
        {'title': "Contact", 'url_name': "contact"}]


def index(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'STEM'
    }
    return render(request, "blog/index.html", context=context)


def blog(request):
    return HttpResponse("BLOG")


def about(request):
    return render(request, "blog/about.html", {"menu": menu, "title": "About"})


def contact(request):
    return HttpResponse("CONTACT")


def show_post(request, post_id):
    return HttpResponse(f"Post = {post_id}")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
