# Generated by Django 2.2.12 on 2021-03-15 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0032_auto_20210315_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='listeners',
            field=models.IntegerField(default=0),
        ),
    ]
