# Generated by Django 2.1.3 on 2019-01-21 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('environment', '0012_auto_20190121_0302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='environment',
            name='user',
        ),
    ]