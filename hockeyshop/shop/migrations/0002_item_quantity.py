# Generated by Django 4.2.4 on 2023-08-22 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.SmallIntegerField(default=1, verbose_name='Количество'),
        ),
    ]
