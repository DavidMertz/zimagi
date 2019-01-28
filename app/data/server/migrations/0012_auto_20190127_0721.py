# Generated by Django 2.1.3 on 2019-01-27 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_auto_20190127_0721'),
        ('server', '0011_auto_20190126_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='firewalls',
            field=models.ManyToManyField(null=True, related_name='servers', to='network.Firewall'),
        ),
        migrations.AlterField(
            model_name='server',
            name='environment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='servers', to='environment.Environment'),
        ),
        migrations.AlterField(
            model_name='server',
            name='groups',
            field=models.ManyToManyField(null=True, related_name='servers', to='server.ServerGroup'),
        ),
        migrations.AlterField(
            model_name='server',
            name='subnet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='servers', to='network.Subnet'),
        ),
    ]
