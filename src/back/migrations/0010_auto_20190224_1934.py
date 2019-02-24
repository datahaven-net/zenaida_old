# Generated by Django 2.1.7 on 2019-02-24 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0009_auto_20190224_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='epp_id',
            field=models.CharField(blank=True, default=None, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='epp_id',
            field=models.CharField(blank=True, default=None, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='registrant',
            name='epp_id',
            field=models.CharField(blank=True, default=None, max_length=32, null=True, unique=True),
        ),
    ]
