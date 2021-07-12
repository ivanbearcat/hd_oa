# Generated by Django 3.2.4 on 2021-07-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0012_auto_20210701_1001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='stauts',
            new_name='status',
        ),
        migrations.AlterField(
            model_name='table',
            name='remote_card_ip',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='远控卡IP'),
        ),
    ]