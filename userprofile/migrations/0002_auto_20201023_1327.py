# Generated by Django 3.0.8 on 2020-10-23 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='approve_data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repair',
            name='completed_data',
            field=models.DateField(blank=True, null=True),
        ),
    ]
