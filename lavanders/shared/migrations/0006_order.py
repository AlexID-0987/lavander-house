# Generated by Django 4.1.3 on 2022-12-24 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0005_remove_products_quantityprod_remove_products_summa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('products', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('summa', models.PositiveIntegerField()),
            ],
        ),
    ]
