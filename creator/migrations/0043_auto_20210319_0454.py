# Generated by Django 2.2.12 on 2021-03-19 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0042_auto_20210319_0449'),
    ]

    operations = [
        migrations.AddField(
            model_name='contents',
            name='visiblity',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='visiblity',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]