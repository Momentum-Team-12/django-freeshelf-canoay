# Generated by Django 4.0.4 on 2022-05-10 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_category_alter_category_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
