# Generated by Django 2.2.12 on 2021-03-14 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0022_auto_20210314_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribtions',
            name='premium',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='playlistcontent',
            name='playlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consumer.Playlist'),
        ),
    ]
