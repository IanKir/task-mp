# Generated by Django 2.2.10 on 2020-04-30 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200501_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='executor',
            field=models.ManyToManyField(blank=True, to='core.Profile'),
        ),
    ]