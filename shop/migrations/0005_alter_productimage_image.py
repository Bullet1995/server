# Generated by Django 5.1.6 on 2025-03-12 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='products/', verbose_name='Изображение'),
        ),
    ]
