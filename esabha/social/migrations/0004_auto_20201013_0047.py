# Generated by Django 3.0.3 on 2020-10-12 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20201013_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.MyProfile'),
        ),
    ]