# Generated by Django 5.0.6 on 2024-06-05 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0011_book_created_at_book_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Narxi'),
        ),
    ]
