# Generated by Django 3.1.5 on 2021-01-28 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_customer_doc_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='doc_num',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
    ]
