# Generated by Django 2.2.9 on 2020-04-29 14:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workpackage',
            name='pid',
            field=models.CharField(default='0_0_0', max_length=11, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='ID doesnt comply', regex='^\\d{1,3}\\_\\d{1,3}_\\d{1,3}$')]),
        ),
    ]