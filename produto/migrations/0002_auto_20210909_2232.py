# Generated by Django 3.2.6 on 2021-09-09 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelo',
            name='foto',
        ),
        migrations.AddField(
            model_name='modelo',
            name='nome',
            field=models.CharField(default='', max_length=255),
        ),
    ]
