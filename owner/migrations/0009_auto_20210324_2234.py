# Generated by Django 2.2.12 on 2021-03-24 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0008_popularshows_toppodcasters_trendingshows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toppodcasters',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
