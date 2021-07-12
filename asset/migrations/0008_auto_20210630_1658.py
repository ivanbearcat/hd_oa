# Generated by Django 3.2.4 on 2021-06-30 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0007_auto_20210622_1703'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='table',
            options={'permissions': (('can_view_password', 'Can view password'),), 'verbose_name_plural': '资产表'},
        ),
        migrations.AddField(
            model_name='table',
            name='_type',
            field=models.CharField(blank=True, choices=[('物理机', '物理机'), ('虚拟机', '虚拟机'), ('交换机', '交换机'), ('防火墙', '防火墙'), ('存储设备', '存储设备')], max_length=16, null=True, verbose_name='类型'),
        ),
        migrations.AddField(
            model_name='table',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='最后更新时间'),
        ),
        migrations.AlterField(
            model_name='table',
            name='checker',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='盘点人'),
        ),
        migrations.AlterField(
            model_name='table',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='登记时间'),
        ),
        migrations.AlterField(
            model_name='table',
            name='new_asset_number',
            field=models.CharField(default='x', max_length=16, verbose_name='新资产编号'),
        ),
        migrations.AlterField(
            model_name='table',
            name='password',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='table',
            name='server_ip',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='主机IP'),
        ),
        migrations.AlterField(
            model_name='table',
            name='ssh_port',
            field=models.IntegerField(blank=True, null=True, verbose_name='ssh端口'),
        ),
        migrations.AlterField(
            model_name='table',
            name='user',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='用户名'),
        ),
    ]
