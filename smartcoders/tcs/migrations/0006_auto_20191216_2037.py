# Generated by Django 3.0 on 2019-12-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcs', '0005_auto_20191216_2036'),
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