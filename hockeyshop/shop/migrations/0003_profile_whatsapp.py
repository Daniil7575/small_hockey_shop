# Generated by Django 4.2.4 on 2023-08-31 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_item_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='Вотсап'),
        ),
    ]