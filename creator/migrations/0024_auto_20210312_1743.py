# Generated by Django 2.2.12 on 2021-03-12 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0023_auto_20210312_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follows',
            name='episodes',
        ),
        migrations.RemoveField(
            model_name='follows',
            name='shows',
        ),
    ]