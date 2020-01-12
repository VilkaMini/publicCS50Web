# Generated by Django 2.0.3 on 2020-01-09 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_toppings_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=5)),
            ],
        ),
        migrations.AlterField(
            model_name='pizza',
            name='kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Kind'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Size'),
        ),
    ]
