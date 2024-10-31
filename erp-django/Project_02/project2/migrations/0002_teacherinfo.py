# Generated by Django 5.0.2 on 2024-02-29 19:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_data', to='project2.teacher')),
                ('TeacherEXP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_data', to='project2.experience')),
            ],
            options={
                'db_table': 'TeacherInfo',
            },
        ),
    ]
