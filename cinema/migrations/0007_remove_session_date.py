# Generated by Django 4.1.3 on 2022-12-10 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0006_session_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='date',
        ),
    ]