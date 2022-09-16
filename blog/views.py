from django.views import generic

from . import models


# Create your views here
class news(generic.ListView):
    model = models.news
    template_name = 'blog/news.html'
    context_object_name = 'news'

