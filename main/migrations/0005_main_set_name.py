# Generated by Django 3.2.8 on 2021-10-23 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211023_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='set_name',
            field=models.TextField(default='-'),
        ),
    ]
