# Generated by Django 4.1.1 on 2022-09-16 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('short_discribtion', models.CharField(max_length=400)),
                ('discribtion', models.TextField()),
                ('image_news', models.ImageField(blank=True, null=True, upload_to='media/news_image')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
