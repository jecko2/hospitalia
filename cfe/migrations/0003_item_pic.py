# Generated by Django 4.1.4 on 2022-12-24 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfe', '0002_heroslider'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='product/'),
        ),
    ]
