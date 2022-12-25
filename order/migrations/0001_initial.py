# Generated by Django 4.1.4 on 2022-12-25 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cfe', '0009_delete_deliverylocation_delete_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=225, verbose_name='Email Address')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cfe.item')),
            ],
        ),
    ]