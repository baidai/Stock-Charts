# Generated by Django 2.2.3 on 2019-07-25 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stc', '0005_auto_20190726_0337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='close',
            old_name='day',
            new_name='date',
        ),
    ]
