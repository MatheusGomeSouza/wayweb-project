# Generated by Django 3.2.6 on 2021-11-01 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='user',
        ),
    ]
