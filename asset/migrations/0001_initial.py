# Generated by Django 3.2.4 on 2021-06-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_ip', models.GenericIPAddressField(unique=True, verbose_name='主机IP')),
                ('ssh_port', models.IntegerField(verbose_name='ssh端口')),
                ('user', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('model', models.CharField(blank=True, max_length=32, null=True, verbose_name='型号')),
                ('sn', models.CharField(blank=True, max_length=16, null=True, verbose_name='序列号')),
                ('cpu', models.CharField(blank=True, max_length=16, null=True, verbose_name='cpu')),
                ('memory', models.CharField(blank=True, max_length=16, null=True, verbose_name='内存')),
                ('disk', models.CharField(blank=True, max_length=16, null=True, verbose_name='硬盘')),
                ('os', models.CharField(blank=True, max_length=32, null=True, verbose_name='操作系统')),
                ('deployment_plan', models.CharField(blank=True, max_length=16, null=True, verbose_name='部署规划')),
                ('doployment_mod', models.CharField(blank=True, max_length=256, null=True, verbose_name='部署模块')),
                ('remote_card_ip', models.GenericIPAddressField(blank=True, null=True, unique=True, verbose_name='远控卡IP')),
                ('remote_card_user', models.CharField(blank=True, max_length=32, null=True, verbose_name='远控卡用户名')),
                ('remote_card_password', models.CharField(blank=True, max_length=32, null=True, verbose_name='远控卡密码')),
                ('organization', models.CharField(blank=True, max_length=32, null=True, verbose_name='组织实体')),
                ('old_asset_number', models.CharField(blank=True, max_length=16, null=True, verbose_name='旧资产编号')),
                ('new_asset_number', models.CharField(blank=True, max_length=16, null=True, verbose_name='新资产编号')),
                ('owner', models.CharField(blank=True, max_length=16, null=True, verbose_name='使用人')),
                ('owner_department', models.CharField(blank=True, max_length=16, null=True, verbose_name='使用部门')),
                ('is_use', models.CharField(blank=True, max_length=16, null=True, verbose_name='使用情况')),
                ('cost_center', models.CharField(blank=True, max_length=16, null=True, verbose_name='成本中心')),
                ('checker', models.CharField(blank=True, max_length=16, null=True, verbose_name='使用人')),
            ],
            options={
                'permissions': (('can_view', 'Can view the page'),),
            },
        ),
    ]
