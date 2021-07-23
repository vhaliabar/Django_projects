# Generated by Django 3.1.5 on 2021-02-20 12:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='nickname',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(3, 'Nickname must be greater than 2 character')]),
        ),
        migrations.AlterField(
            model_name='make',
            name='name',
            field=models.CharField(help_text='Enter a make (e.g. Hyundai)', max_length=200, validators=[django.core.validators.MinLengthValidator(3, 'Make must be greater than 2 character')]),
        ),
    ]