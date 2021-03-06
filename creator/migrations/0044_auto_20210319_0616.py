# Generated by Django 2.2.12 on 2021-03-19 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0043_auto_20210319_0454'),
    ]

    operations = [
        migrations.AddField(
            model_name='contents',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='contents',
            name='created_time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='contents',
            name='date_of_published',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contents',
            name='time_of_published',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
