from django.urls import path
from . import views
urlpatterns = [
    path('news/', views.news.as_view(), name='blog_news_list'),
    # path('news/<int:pk>/', views., name='news_detail_view')
]