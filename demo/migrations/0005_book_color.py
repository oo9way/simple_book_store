# Generated by Django 5.0.6 on 2024-06-05 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_alter_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='color',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
