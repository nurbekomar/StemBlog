# Generated by Django 4.2.5 on 2023-09-16 06:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_blog_subtitle"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="subtitle",
        ),
    ]