# Generated by Django 3.0.3 on 2020-10-14 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_auto_20201013_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='pic',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='pic',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]