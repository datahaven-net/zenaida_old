# Generated by Django 2.1.5 on 2019-02-03 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0004_auto_20190120_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='contact_admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_domains', to='back.Contact', verbose_name='Administrative'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='contact_billing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billing_domains', to='back.Contact', verbose_name='Billing'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='contact_tech',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tech_domains', to='back.Contact', verbose_name='Technical'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='nameserver1',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='Nameserver 1'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='nameserver2',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='Nameserver 2'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='nameserver3',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='Nameserver 3'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='nameserver4',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='Nameserver 4'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_city',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_country',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_postal_code',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='ZIP code'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_province',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Province'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_street',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Street address'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact_email',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact_fax',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Fax'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact_voice',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Mobile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='organization_name',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Organization'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='person_name',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Full Name'),
        ),
    ]