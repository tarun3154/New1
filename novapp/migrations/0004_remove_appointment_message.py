# Generated by Django 4.2.3 on 2023-08-06 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novapp', '0003_patient_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='message',
        ),
    ]
