# Generated by Django 2.0.1 on 2018-02-16 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fec', '0004_schedulea'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedulea',
            old_name='contributor_first_nam',
            new_name='contributor_first_name',
        ),
    ]