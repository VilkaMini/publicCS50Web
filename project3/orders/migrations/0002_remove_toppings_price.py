# Generated by Django 2.0.3 on 2020-01-09 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toppings',
            name='price',
        ),
    ]
