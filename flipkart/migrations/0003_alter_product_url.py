# Generated by Django 4.1.5 on 2023-01-31 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.URLField(),
        ),
    ]