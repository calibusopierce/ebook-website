# Generated by Django 3.0.14 on 2022-03-06 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_customer_phone_field'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
