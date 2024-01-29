# Generated by Django 5.0.1 on 2024-01-29 05:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CloudPark', '0002_alter_contract_max_value_alter_customer_card_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_plan',
            name='Due_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='parkmovement',
            name='Entry_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='parkmovement',
            name='Exit_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]