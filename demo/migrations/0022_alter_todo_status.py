# Generated by Django 5.0.6 on 2024-06-21 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0021_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('not_started', 'Boshlanmagan'), ('started', 'Jarayonda'), ('finished', 'Tugatilgan')], default='not_started', max_length=16),
        ),
    ]
