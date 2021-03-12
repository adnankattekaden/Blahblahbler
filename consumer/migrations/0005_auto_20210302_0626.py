# Generated by Django 3.1.7 on 2021-03-02 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0007_show_thumbnail'),
        ('consumer', '0004_auto_20210228_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='content',
        ),
        migrations.CreateModel(
            name='PlaylistContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='creator.contents')),
                ('playlist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consumer.playlist')),
            ],
        ),
    ]