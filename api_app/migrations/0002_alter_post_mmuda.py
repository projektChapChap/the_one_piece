# Generated by Django 3.2.8 on 2021-10-08 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='mmuda',
            field=models.TimeField(),
        ),
    ]