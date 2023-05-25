# Generated by Django 4.2 on 2023-05-24 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("head_image", models.ImageField(blank=True, upload_to="")),
                ("content", models.TextField()),
                ("created_at", models.DateField(auto_now_add=True)),
                (
                    "file_upload",
                    models.FileField(blank=True, upload_to="blog/files/%Y/%m/%d/"),
                ),
            ],
        ),
    ]