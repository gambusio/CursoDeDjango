# Generated by Django 4.1.5 on 2023-02-26 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_comments_signature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='signature',
            field=models.CharField(default='noSign', max_length=127),
        ),
    ]
