# Generated by Django 4.1.5 on 2023-03-05 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_until',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
