from django.db import models
from django.urls import reverse

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Текст статья")
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата записи")
    time_update = models.DateTimeField(
        auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey(
        'Category', on_delete=models.PROTECT, null=True, verbose_name="Категория")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["time_create", "title"]


class Category(models.Model):
    name = models.CharField(
        max_length=255, db_index=True, verbose_name="Названия")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_id": self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
