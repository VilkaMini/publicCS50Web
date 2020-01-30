# Generated by Django 2.1.5 on 2020-01-21 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200114_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='dinner',
            name='largePrice',
            field=models.IntegerField(default=65),
        ),
        migrations.AddField(
            model_name='dinner',
            name='smallPrice',
            field=models.IntegerField(default=40),
        ),
        migrations.AddField(
            model_name='pasta',
            name='price',
            field=models.IntegerField(default=8.75),
        ),
        migrations.AddField(
            model_name='salads',
            name='price',
            field=models.IntegerField(default=8.25),
        ),
        migrations.AddField(
            model_name='sub',
            name='largePrice',
            field=models.IntegerField(default=7.95),
        ),
        migrations.AddField(
            model_name='sub',
            name='smallPrice',
            field=models.IntegerField(default=6.5),
        ),
    ]