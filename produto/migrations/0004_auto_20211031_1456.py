# Generated by Django 3.2.6 on 2021-10-31 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_auto_20211010_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='feminino',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='masculino',
            field=models.BooleanField(default=False),
        ),
    ]
