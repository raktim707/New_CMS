# Generated by Django 3.2.8 on 2021-10-23 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20211023_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='fb',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AlterField(
            model_name='main',
            name='link',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AlterField(
            model_name='main',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='main',
            name='set_name',
            field=models.TextField(default='-', max_length=30),
        ),
        migrations.AlterField(
            model_name='main',
            name='tell',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AlterField(
            model_name='main',
            name='tw',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AlterField(
            model_name='main',
            name='yt',
            field=models.CharField(default='-', max_length=30),
        ),
    ]