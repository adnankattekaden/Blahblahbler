# Generated by Django 2.2.12 on 2021-03-14 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0023_auto_20210314_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribtions',
            name='premium',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='premium',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='playlistcontent',
            name='playlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consumer.Playlist'),
        ),
    ]
