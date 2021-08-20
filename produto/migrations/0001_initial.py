# Generated by Django 3.2.6 on 2021-08-16 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Peca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamanho', models.CharField(max_length=255)),
                ('cor', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(max_length=255)),
                ('preco', models.IntegerField()),
                ('gereno', models.CharField(blank=True, max_length=255, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.categoria')),
                ('peca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.peca')),
            ],
        ),
    ]
