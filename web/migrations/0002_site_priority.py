# Generated by Django 2.0.13 on 2020-03-14 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='priority',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]