from django.contrib import admin

from blog.models import *

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create", "is_published")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    list_editable = ("is_published",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Blog, BlogAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name", )
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
