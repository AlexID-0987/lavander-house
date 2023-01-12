# Generated by Django 4.1.3 on 2022-12-23 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0003_order_products_alter_products_photo_orderperson_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderperson',
            name='ProductsId',
        ),
        migrations.AddField(
            model_name='products',
            name='quantityProd',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='summa',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Order_Products',
        ),
        migrations.DeleteModel(
            name='OrderPerson',
        ),
    ]
