# Generated by Django 4.1.3 on 2023-01-07 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0002_alter_owner_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
