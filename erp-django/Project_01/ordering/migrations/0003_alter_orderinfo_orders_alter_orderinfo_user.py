# Generated by Django 5.0.2 on 2024-03-02 08:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0002_alter_orderinfo_orders_alter_orderinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='orders',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Menu', to='ordering.menu'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to='ordering.user'),
        ),
    ]