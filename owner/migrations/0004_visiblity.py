# Generated by Django 2.2.12 on 2021-03-19 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0003_advertisement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visiblity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visiblity_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]