# Generated by Django 2.2 on 2019-07-03 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_auto_20190703_1407'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='logmessage',
            table='core_log_messages',
        ),
    ]
