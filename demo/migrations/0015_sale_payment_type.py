# Generated by Django 5.0.6 on 2024-06-19 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0014_remove_book_authors_alter_book_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='payment_type',
            field=models.CharField(choices=[('naqd', 'Naqd'), ('card', 'Karta')], default='naqd', max_length=4, verbose_name="To'lov turi"),
            preserve_default=False,
        ),
    ]
