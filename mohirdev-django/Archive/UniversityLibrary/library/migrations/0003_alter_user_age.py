# Generated by Django 5.0.2 on 2024-02-29 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]
