from django.urls import path
from blog.views import *

urlpatterns = [
    path("", index),
    path("about/", about)
]
