# Generated by Django 3.2.12 on 2024-05-24 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='firstname',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='account',
            name='lastname',
            field=models.CharField(default='', max_length=150),
        ),
    ]
