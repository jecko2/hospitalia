# Generated by Django 4.1.4 on 2022-12-24 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider', models.ImageField(upload_to='slider/')),
            ],
        ),
    ]
