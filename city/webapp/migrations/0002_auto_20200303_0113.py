# Generated by Django 3.0.3 on 2020-03-03 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='media',
            new_name='file',
        ),
    ]
