# Generated by Django 4.2.1 on 2023-08-07 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novapp', '0005_remove_appointment_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dob',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='symptoms',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]