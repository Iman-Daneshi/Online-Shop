# Generated by Django 3.2.16 on 2022-10-04 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='store/placeholder.png', upload_to='store/'),
        ),
    ]
