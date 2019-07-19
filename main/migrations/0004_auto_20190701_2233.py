# Generated by Django 2.2.2 on 2019-07-01 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190701_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_series',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_slug',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 1, 22, 33, 0, 50647), verbose_name='date published'),
        ),
    ]