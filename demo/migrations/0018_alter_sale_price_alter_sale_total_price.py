# Generated by Django 5.0.6 on 2024-06-19 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0017_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='price',
            field=models.IntegerField(default=0, editable=False, verbose_name='Sotilgan narxi'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='total_price',
            field=models.IntegerField(default=0, editable=False, verbose_name='Umumiy savdo'),
        ),
    ]