# Generated by Django 2.2.12 on 2021-03-14 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.FloatField()),
                ('validity', models.IntegerField()),
            ],
        ),
    ]