# Generated by Django 2.2.10 on 2020-04-04 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mindapp', '0036_auto_20200404_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='countdown',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='config',
            name='time',
            field=models.CharField(default=1, max_length=40),
        ),
        migrations.AlterField(
            model_name='situationtimer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mindapp.Player'),
        ),
    ]
