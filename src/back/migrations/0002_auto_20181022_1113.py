# Generated by Django 2.1.2 on 2018-10-22 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='auth_key',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='domain',
            name='contact_admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_domains', to='back.Contact'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='contact_billing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billing_domains', to='back.Contact'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='contact_tech',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tech_domains', to='back.Contact'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='epp_id',
            field=models.CharField(blank=True, default='', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='registrant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registrant_domains', to='back.Contact'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='registrar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domains', to='back.Registrar'),
        ),
    ]