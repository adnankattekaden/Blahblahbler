# Generated by Django 2.2.12 on 2021-03-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0033_auto_20210315_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='contents',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
