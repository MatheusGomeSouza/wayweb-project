# Generated by Django 3.2.6 on 2021-11-26 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_trackingcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.CharField(default='', max_length=2, verbose_name='Tamanho'),
        ),
        migrations.AddField(
            model_name='item',
            name='size_number',
            field=models.CharField(default='', max_length=2, verbose_name='Tamanho por número'),
        ),
    ]
