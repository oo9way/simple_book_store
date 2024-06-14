# Generated by Django 5.0.6 on 2024-06-14 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0013_sale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AlterModelOptions(
            name='book',
            options={},
        ),
        migrations.RemoveField(
            model_name='book',
            name='color',
        ),
        migrations.RemoveField(
            model_name='book',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='book',
            name='description',
        ),
        migrations.RemoveField(
            model_name='book',
            name='published_at',
        ),
        migrations.RemoveField(
            model_name='book',
            name='year',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='amount',
        ),
        migrations.AddField(
            model_name='sale',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Savdo sanasi'),
        ),
        migrations.AddField(
            model_name='sale',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Sotilgan narxi'),
        ),
        migrations.AddField(
            model_name='sale',
            name='qty',
            field=models.PositiveIntegerField(default=0, verbose_name='Sotilgan soni'),
        ),
        migrations.AddField(
            model_name='sale',
            name='total_price',
            field=models.IntegerField(default=0, verbose_name='Umumiy savdo'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.PositiveIntegerField(verbose_name='ISBN kodi'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Narxi'),
        ),
        migrations.AlterField(
            model_name='book',
            name='qty',
            field=models.PositiveIntegerField(default=0, verbose_name='Bazadagi soni'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sales', to='demo.book'),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
