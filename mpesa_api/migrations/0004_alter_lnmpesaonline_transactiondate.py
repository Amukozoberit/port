# Generated by Django 3.2.8 on 2021-10-20 10:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa_api', '0003_auto_20211020_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lnmpesaonline',
            name='TransactionDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
