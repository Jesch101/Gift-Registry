# Generated by Django 4.0 on 2022-04-05 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift_registry', '0011_alter_gifter_unique_together_gifter_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='claimed',
            field=models.BooleanField(default=False),
        ),
    ]
