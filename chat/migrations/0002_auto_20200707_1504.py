# Generated by Django 3.0.8 on 2020-07-07 19:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('login', '0002_auto_20200706_2014'),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FriendRequestmaster',
            new_name='Msgmaster',
        ),
    ]
