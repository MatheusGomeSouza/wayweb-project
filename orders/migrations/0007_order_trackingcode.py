# Generated by Django 3.2.6 on 2021-11-26 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_freight'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='trackingCode',
            field=models.CharField(blank=True, default='', max_length=250, verbose_name='CodigoRastreio'),
        ),
    ]
