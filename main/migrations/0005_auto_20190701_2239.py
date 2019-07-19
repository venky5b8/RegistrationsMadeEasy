# Generated by Django 2.2.2 on 2019-07-01 17:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190701_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.TutorialSeries', verbose_name='Series'),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_slug',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 1, 22, 39, 18, 954230), verbose_name='date published'),
        ),
    ]
