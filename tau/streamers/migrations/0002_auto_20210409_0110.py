# Generated by Django 3.1.7 on 2021-04-09 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamer',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
