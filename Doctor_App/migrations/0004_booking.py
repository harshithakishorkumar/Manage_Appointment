# Generated by Django 4.1.7 on 2023-03-11 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor_App', '0003_patient_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doctor_Id', models.CharField(default=None, max_length=100)),
                ('Patient_Id', models.CharField(default=None, max_length=100)),
                ('Slot', models.CharField(default=None, max_length=100)),
                ('Timing', models.CharField(default=None, max_length=100)),
            ],
            options={
                'db_table': 'Booking',
            },
        ),
    ]