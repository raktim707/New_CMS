# Generated by Django 3.2.8 on 2021-10-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20211025_0657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='pic',
            new_name='picname',
        ),
        migrations.AddField(
            model_name='articles',
            name='picurl',
            field=models.TextField(default='-'),
        ),
    ]
