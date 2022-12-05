# Generated by Django 4.1.3 on 2022-12-05 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cinema', '0001_initial'),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cinema.seat'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='booking.session'),
        ),
    ]
