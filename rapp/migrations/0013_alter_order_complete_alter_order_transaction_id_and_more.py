# Generated by Django 4.1 on 2022-08-18 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rapp', '0012_alter_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rapp.order'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rapp.product'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
