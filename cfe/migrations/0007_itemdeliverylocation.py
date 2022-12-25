# Generated by Django 4.1.4 on 2022-12-25 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cfe', '0006_alter_itemhighlights_highlight_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemDeliveryLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30, verbose_name='Delivery Location')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_delivery_location', to='cfe.item')),
            ],
        ),
    ]
