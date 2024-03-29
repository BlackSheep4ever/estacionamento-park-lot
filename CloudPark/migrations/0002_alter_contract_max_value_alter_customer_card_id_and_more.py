# Generated by Django 5.0.1 on 2024-01-27 22:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CloudPark', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='Max_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Card_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customer_plan',
            name='Due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='parkmovement',
            name='Exit_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='parkmovement',
            name='Value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='Customer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CloudPark.customer'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='Description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='Model',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
