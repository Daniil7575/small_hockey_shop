# Generated by Django 4.2.4 on 2023-10-07 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_profile_whatsapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='other_contacts',
            field=models.TextField(blank=True, null=True, verbose_name='Другие виды связи'),
        ),
    ]