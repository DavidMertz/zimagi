# Generated by Django 2.1.3 on 2019-02-06 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0016_auto_20190204_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='_variables',
            field=models.TextField(db_column='variables', default='{}'),
        ),
    ]