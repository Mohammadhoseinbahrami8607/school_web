from django.db import models

from config import settings


# Create your models here.
class news(models.Model):
    title = models.CharField(max_length=50)
    short_discribtion = models.CharField(max_length=400)
    discribtion = models.TextField()
    image_news = models.ImageField(upload_to='media/news_image', null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.user}'
