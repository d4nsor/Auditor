# Generated by Django 3.2 on 2021-05-28 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modo_monitor', '0002_access_point_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='access_point',
            name='device_id',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
