# Generated by Django 4.2.3 on 2023-07-11 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_product_des'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='des',
            new_name='description',
        ),
    ]
