# Generated by Django 3.0.3 on 2020-03-06 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200303_0113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='file',
            new_name='media',
        ),
    ]
