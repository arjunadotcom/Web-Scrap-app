# Generated by Django 4.1.5 on 2023-02-01 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0005_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='product_images'),
        ),
    ]
