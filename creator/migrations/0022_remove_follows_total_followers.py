# Generated by Django 2.2.12 on 2021-03-12 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0021_auto_20210312_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follows',
            name='total_followers',
        ),
    ]
