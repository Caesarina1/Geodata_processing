# Generated by Django 4.2.2 on 2023-07-09 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo_base', '0002_meta'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Meta',
        ),
        migrations.AlterModelOptions(
            name='target',
            options={'permissions': (('can_view_data_transfer', 'Can view data transfer page'), ('can_view_position', 'Can view position page'))},
        ),
    ]