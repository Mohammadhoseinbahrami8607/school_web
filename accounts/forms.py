from django.forms import Form
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from . import models


class CoustomuserCrationForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = ['father_name', 'first_name', 'last_name', 'password', 'username']


class CoustomUserChangeForm(UserChangeForm):
    class Meta:
        model = models.CustomUser
        fields = ['password', 'father_name', 'first_name', 'last_name', 'username']
