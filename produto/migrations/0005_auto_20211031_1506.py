# Generated by Django 3.2.6 on 2021-10-31 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_auto_20211031_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='feminino',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='masculino',
            field=models.BooleanField(default=True),
        ),
    ]