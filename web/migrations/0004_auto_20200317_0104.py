# Generated by Django 2.0.13 on 2020-03-16 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20200316_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='row',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='web.Row'),
        ),
    ]
