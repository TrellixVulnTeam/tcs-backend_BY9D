# Generated by Django 3.0 on 2019-12-16 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcs', '0003_trains_tr_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trains',
            name='arr',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='trains',
            name='dep',
            field=models.TimeField(),
        ),
    ]