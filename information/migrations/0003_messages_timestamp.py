# Generated by Django 3.0.6 on 2020-05-17 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_auto_20200517_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='timestamp',
            field=models.CharField(default='0', max_length=255),
        ),
    ]
