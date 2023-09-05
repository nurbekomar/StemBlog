from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from blog.models import *
# Create your views here.

menu = ["О Сайте", "Добавить", "Удалить", "Сохранить"]


def index(request):
    posts = Blog.objects.all()
    return render(request, "blog/index.html", {"posts": posts, "menu": menu, "title": "Main Page"})


def about(request):
    return render(request, "blog/about.html", {"menu": menu, "title": "About"})


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
