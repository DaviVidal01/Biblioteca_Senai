# Generated by Django 4.2.4 on 2023-10-03 22:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0006_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='data_Dev',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 3, 19, 45, 32, 149090)),
        ),
        migrations.AlterField(
            model_name='registro',
            name='data_Ret',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 3, 19, 45, 32, 149090)),
        ),
    ]
