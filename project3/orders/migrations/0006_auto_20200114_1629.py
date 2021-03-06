# Generated by Django 2.1.5 on 2020-01-14 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_dinner_dinnerplate_pasta_pastas_salad_salads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinnerplate',
            name='plate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Dinner'),
        ),
        migrations.AlterField(
            model_name='salad',
            name='salad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saladOrder', to='orders.Salads'),
        ),
    ]
