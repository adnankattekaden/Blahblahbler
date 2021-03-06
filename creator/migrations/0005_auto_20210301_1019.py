# Generated by Django 3.1.7 on 2021-03-01 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0004_show_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='podcast_name',
            new_name='description',
        ),
        migrations.AddField(
            model_name='show',
            name='show_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='total_episodes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
