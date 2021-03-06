# Generated by Django 3.0.5 on 2021-06-09 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modo_monitor', '0005_device_device_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='access_point',
            old_name='cipher',
            new_name='auth_crypto',
        ),
        migrations.RenameField(
            model_name='access_point',
            old_name='canal',
            new_name='channel',
        ),
        migrations.RenameField(
            model_name='access_point',
            old_name='suite',
            new_name='cipher_algorithm',
        ),
        migrations.RenameField(
            model_name='access_point',
            old_name='frecuencia',
            new_name='distance_ap',
        ),
        migrations.RenameField(
            model_name='access_point',
            old_name='fspl',
            new_name='frecuency',
        ),
        migrations.RenameField(
            model_name='access_point',
            old_name='encriptacion',
            new_name='security_protocol',
        ),
        migrations.RenameField(
            model_name='access_point',
            old_name='essid',
            new_name='ssid',
        ),
        migrations.AlterField(
            model_name='access_point',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
