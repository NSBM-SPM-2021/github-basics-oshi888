# Generated by Django 3.2.7 on 2021-09-06 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('author', models.CharField(max_length=100, verbose_name='author')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                # ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
            ],
        ),
    ]
