# Generated by Django 3.1.5 on 2021-01-09 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='documents',
            field=models.ManyToManyField(to='core.Document'),
        ),
    ]
