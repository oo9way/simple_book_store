# Generated by Django 5.0.6 on 2024-06-05 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_alter_book_isbn_alter_book_price_alter_book_qty_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Kitob', 'verbose_name_plural': 'Kitoblar'},
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='OO bratim', verbose_name='Tavsifi'),
            preserve_default=False,
        ),
    ]
