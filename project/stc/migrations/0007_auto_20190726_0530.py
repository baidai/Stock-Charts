# Generated by Django 2.2.3 on 2019-07-25 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stc', '0006_auto_20190726_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='close',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
