# Generated by Django 3.2.4 on 2021-06-30 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0010_alter_table_new_asset_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='name',
            field=models.CharField(blank=True, default='x', max_length=64, null=True, verbose_name='资产名称'),
        ),
    ]
