# Generated by Django 4.1.7 on 2023-03-11 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor_App', '0006_remove_patient_details_treatment_booking_treatment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_Id', models.CharField(default=None, max_length=100)),
                ('Feedback', models.CharField(default=None, max_length=300)),
            ],
            options={
                'db_table': 'Feedback',
            },
        ),
    ]
