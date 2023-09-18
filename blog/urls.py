from django.urls import path
from blog.views import *

urlpatterns = [
    path("", index, name="home"),
    path("blog/", blog, name="blog"),
    path("about/", about, name="about"),
    path("post/<int:post_id>", show_post, name="post"),
    path("category/<int:cat_id>", show_category, name="category")
]
