# Generated by Django 3.2.8 on 2021-11-12 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ImageOrVideo', models.FileField(upload_to='static/uploads', verbose_name='ImageOrVideo')),
            ],
        ),
    ]
