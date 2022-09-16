from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    father_name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='user_picture', null=True, blank=True)


class Exam(models.Model):
    SUBJECT = (
        ('ریاضی', 'ریاضی'),
        ('علوم', 'علوم'),
        ('ادبیات', 'ادبیات'),

    )
    subject = models.CharField(choices=SUBJECT, max_length=20)
    author = models.CharField(max_length=4000)
    datetime = models.DateTimeField(auto_now_add=True)
    tedad_soal = models.PositiveIntegerField(default=10)
    time = models.TimeField()
    modat_zaman = models.CharField(max_length=1000, default='10 دقیقه')


class Soal(models.Model):
    quastion_picture = models.ImageField(upload_to='quation_picture', null=True, blank=True)
    quastion = models.TextField(null=True, blank=True)
    option1 = models.CharField(max_length=3000)
    option2 = models.CharField(max_length=3000)
    option3 = models.CharField(max_length=3000)
    option4 = models.CharField(max_length=3000)
    True_option = models.PositiveIntegerField()
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='soalat')

    def __str__(self):
        return f'{self.pk}'

