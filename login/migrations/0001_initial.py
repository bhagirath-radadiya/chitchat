# Generated by Django 3.0.8 on 2020-07-06 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loginmaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginUserName', models.CharField(max_length=100)),
                ('loginPassword', models.CharField(max_length=50)),
                ('loginRole', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usermaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=100)),
                ('userMobileNo', models.CharField(blank=True, max_length=10, null=True)),
                ('userBirthdate', models.DateField(blank=True, null=True)),
                ('userAddress', models.CharField(blank=True, max_length=1000, null=True)),
                ('userFacebook', models.CharField(blank=True, max_length=1000, null=True)),
                ('userTwitter', models.CharField(blank=True, max_length=1000, null=True)),
                ('userInstagram', models.CharField(blank=True, max_length=1000, null=True)),
                ('userLinkedin', models.CharField(blank=True, max_length=1000, null=True)),
                ('userProfilePhoto', models.CharField(blank=True, max_length=10, null=True)),
                (
                    'user_LoginId',
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Loginmaster')),
            ],
        ),
    ]