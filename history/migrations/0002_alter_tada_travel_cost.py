# Generated by Django 3.2.8 on 2021-10-12 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tada',
            name='travel_cost',
            field=models.IntegerField(),
        ),
    ]
