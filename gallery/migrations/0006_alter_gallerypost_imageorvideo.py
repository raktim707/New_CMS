# Generated by Django 3.2.8 on 2021-11-12 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_alter_gallerypost_imageorvideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerypost',
            name='ImageOrVideo',
            field=models.FileField(upload_to='media/gallery/'),
        ),
    ]
