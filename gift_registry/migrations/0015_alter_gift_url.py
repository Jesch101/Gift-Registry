# Generated by Django 4.0 on 2022-04-07 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift_registry', '0014_alter_gift_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='url',
            field=models.URLField(blank=True, default=''),
        ),
    ]
