# Generated by Django 2.2.12 on 2021-03-12 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0019_auto_20210312_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follows',
            name='followed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follow_followed', to=settings.AUTH_USER_MODEL),
        ),
    ]