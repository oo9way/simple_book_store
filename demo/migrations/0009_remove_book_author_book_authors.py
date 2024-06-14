# Generated by Django 5.0.6 on 2024-06-05 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0008_alter_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='demo.author'),
        ),
    ]