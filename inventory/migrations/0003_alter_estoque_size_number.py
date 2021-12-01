# Generated by Django 3.2.6 on 2021-11-26 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_estoque_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='size_number',
            field=models.CharField(blank=True, choices=[('1', '46'), ('2', '48'), ('3', '50'), ('4', '52')], default='', max_length=2, verbose_name='Tamanho'),
        ),
    ]