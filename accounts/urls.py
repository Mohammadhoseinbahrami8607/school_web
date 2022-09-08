from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.Sign_up.as_view(), name = 'sign_up')
]
