from django.shortcuts import render
from django.views import generic
from . import models, forms
from django.urls import reverse_lazy


# Create your views here.
class Sign_up(generic.CreateView):
    model = models
    template_name = 'accounts/sign_up.html'
    form_class = forms.CoustomuserCrationForm
    success_url = reverse_lazy('login')
