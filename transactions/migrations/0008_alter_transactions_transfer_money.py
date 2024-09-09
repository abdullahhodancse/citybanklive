# Generated by Django 5.0.6 on 2024-09-08 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_remove_transactions_account_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='transfer_money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
