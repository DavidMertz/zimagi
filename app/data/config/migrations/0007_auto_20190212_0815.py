# Generated by Django 2.1.3 on 2019-02-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0006_auto_20190212_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='_value',
            field=models.TextField(db_column='value', null=True),
        ),
    ]