# Generated by Django 3.0.8 on 2020-07-07 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('login', '0001_initial'),
        ('friends', '0003_auto_20200706_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequestmaster',
            name='friendRequest_From',
            field=models.ForeignKey(db_column='friendRequest_From', on_delete=django.db.models.deletion.CASCADE,
                                    related_name='friendRequest_From', to='login.Loginmaster'),
        ),
        migrations.AlterField(
            model_name='friendrequestmaster',
            name='friendRequest_To',
            field=models.ForeignKey(db_column='friendRequest_To', on_delete=django.db.models.deletion.CASCADE,
                                    related_name='friendRequest_To', to='login.Loginmaster'),
        ),
    ]
