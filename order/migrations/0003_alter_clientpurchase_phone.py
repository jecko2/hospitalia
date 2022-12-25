# Generated by Django 4.1.4 on 2022-12-25 13:13

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_clientpurchase_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientpurchase',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='KE', verbose_name='Phone Number'),
        ),
    ]
