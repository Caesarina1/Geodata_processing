# Generated by Django 4.2.2 on 2023-06-14 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]