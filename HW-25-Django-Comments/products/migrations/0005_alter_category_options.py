# Generated by Django 4.2.1 on 2023-06-08 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_category_parent_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
