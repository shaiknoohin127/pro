# Generated by Django 3.2.8 on 2021-10-22 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productcurdrestapis', '0002_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='picture',
        ),
    ]