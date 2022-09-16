# Generated by Django 4.1.1 on 2022-09-11 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('ریاضی', 'ریاضی'), ('علوم', 'علوم'), ('ادبیات', 'ادبیات')], max_length=20)),
                ('author', models.CharField(max_length=4000)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('tedad_soal', models.PositiveIntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Soal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quastion_picture', models.ImageField(blank=True, null=True, upload_to='quation_picture')),
                ('quastion', models.TextField(blank=True, null=True)),
                ('option1', models.CharField(max_length=3000)),
                ('option2', models.CharField(max_length=3000)),
                ('option3', models.CharField(max_length=3000)),
                ('option4', models.CharField(max_length=3000)),
                ('True_option', models.PositiveIntegerField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soalat', to='accounts.exam')),
            ],
        ),
    ]
