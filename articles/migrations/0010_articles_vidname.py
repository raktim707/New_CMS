# Generated by Django 3.2.8 on 2021-11-12 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_articles_vidurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='vidname',
            field=models.TextField(default='-'),
            preserve_default=False,
        ),
    ]
