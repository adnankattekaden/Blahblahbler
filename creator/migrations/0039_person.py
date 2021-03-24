# Generated by Django 2.2.12 on 2021-03-19 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0038_visiblity_visiblity_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('shirt_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
            ],
        ),
    ]