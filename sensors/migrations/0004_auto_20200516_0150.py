# Generated by Django 3.0.6 on 2020-05-15 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('sensors', '0003_auto_20200516_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor_device',
            name='home_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.Home'),
        ),
    ]
