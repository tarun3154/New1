# Generated by Django 4.2.3 on 2023-08-06 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
    ]
