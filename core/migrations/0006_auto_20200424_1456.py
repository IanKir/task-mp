# Generated by Django 2.2.10 on 2020-04-24 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_task_executor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]