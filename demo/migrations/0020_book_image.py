# Generated by Django 5.0.6 on 2024-06-19 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0019_alter_sale_book_alter_sale_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book_images'),
        ),
    ]