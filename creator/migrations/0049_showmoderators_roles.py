# Generated by Django 2.2.12 on 2021-03-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0048_showmoderators'),
    ]

    operations = [
        migrations.AddField(
            model_name='showmoderators',
            name='roles',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]