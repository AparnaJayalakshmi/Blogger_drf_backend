# Generated by Django 5.0.3 on 2024-03-07 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='owner',
        ),
    ]