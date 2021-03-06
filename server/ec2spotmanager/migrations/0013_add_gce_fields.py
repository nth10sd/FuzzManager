# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-17 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ec2spotmanager', '0012_add_instance_provider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poolconfiguration',
            old_name='ec2_tags',
            new_name='instance_tags',
        ),
        migrations.RenameField(
            model_name='poolconfiguration',
            old_name='ec2_max_price',
            new_name='max_price',
        ),
        migrations.RenameField(
            model_name='poolconfiguration',
            old_name='userdata_macros',
            new_name='ec2_userdata_macros',
        ),
        migrations.RenameField(
            model_name='poolconfiguration',
            old_name='userdata_file',
            new_name='ec2_userdata_file',
        ),
        migrations.AddField(
            model_name='poolconfiguration',
            name='gce_args',
            field=models.CharField(blank=True, max_length=4095, null=True),
        ),
        migrations.AddField(
            model_name='poolconfiguration',
            name='gce_cmd',
            field=models.CharField(blank=True, max_length=4095, null=True),
        ),
        migrations.AddField(
            model_name='poolconfiguration',
            name='gce_container_name',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='poolconfiguration',
            name='gce_disk_size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='poolconfiguration',
            name='gce_docker_privileged',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poolconfiguration',
            name='gce_env',
            field=models.CharField(blank=True, max_length=4095, null=True),
        ),
        migrations.AddField(
            model_name='poolconfiguration',
            name='gce_env_include_macros',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poolconfiguration',
            name='gce_image_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='poolconfiguration',
            name='gce_machine_types',
            field=models.CharField(blank=True, max_length=4095, null=True),
        ),
        migrations.AddField(
            model_name='poolconfiguration',
            name='gce_raw_config',
            field=models.CharField(blank=True, max_length=4095, null=True),
        ),
    ]
