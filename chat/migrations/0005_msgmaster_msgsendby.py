# Generated by Django 3.0.8 on 2020-07-08 15:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('chat', '0004_msgmaster_msgsenddate'),
    ]

    operations = [
        migrations.AddField(
            model_name='msgmaster',
            name='msgSendBy',
            field=models.IntegerField(null=True),
        ),
    ]
