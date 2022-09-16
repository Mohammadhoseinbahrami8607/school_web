from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.CustomUser)
admin.site.register(models.Exam)
admin.site.register(models.Soal)