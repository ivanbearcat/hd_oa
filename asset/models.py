from django.db import models

class table(models.Model):
    class Meta:
        verbose_name_plural = '资产表'
        permissions = (
            ("can_view", "Can view the page"),
        )

    server_ip = models.GenericIPAddressField(verbose_name='主机IP', blank=False, null=False, unique=True)
    ssh_port = models.IntegerField(verbose_name='ssh端口', blank=False, null=False)
    user = models.CharField(verbose_name='用户名', max_length=32, blank=False, null=False)
    password = models.CharField(verbose_name='密码', max_length=32, blank=False, null=False)
    model = models.CharField(verbose_name='型号', max_length=32, blank=True, null=True)
    sn = models.CharField(verbose_name='序列号', max_length=16, blank=True, null=True)
    cpu = models.CharField(verbose_name='cpu', max_length=16, blank=True, null=True)
    memory = models.CharField(verbose_name='内存', max_length=16, blank=True, null=True)
    disk = models.CharField(verbose_name='硬盘', max_length=16, blank=True, null=True)
    os = models.CharField(verbose_name='操作系统', max_length=64, blank=True, null=True)
    deployment_plan = models.CharField(verbose_name='部署规划', max_length=32, blank=True, null=True)
    doployment_mod = models.CharField(verbose_name='部署模块', max_length=256, blank=True, null=True)
    remote_card_ip = models.GenericIPAddressField(verbose_name='远控卡IP', blank=True, null=True, unique=True)
    remote_card_user = models.CharField(verbose_name='远控卡用户名', max_length=32, blank=True, null=True)
    remote_card_password = models.CharField(verbose_name='远控卡密码', max_length=32, blank=True, null=True)
    organization = models.CharField(verbose_name='组织实体', max_length=32, blank=True, null=True)
    old_asset_number = models.CharField(verbose_name='旧资产编号', max_length=16, blank=True, null=True)
    new_asset_number = models.CharField(verbose_name='新资产编号', max_length=16, blank=True, null=True)
    owner = models.CharField(verbose_name='使用人', max_length=16, blank=True, null=True)
    owner_department = models.CharField(verbose_name='使用部门', max_length=16, blank=True, null=True)
    is_use = models.CharField(verbose_name='使用情况', max_length=16, blank=True, null=True)
    cost_center = models.CharField(verbose_name='成本中心', max_length=16, blank=True, null=True)
    checker = models.CharField(verbose_name='使用人', max_length=16, blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='最后更新时间', auto_now_add=True)
    location = models.CharField(verbose_name='位置', max_length=32, blank=True, null=True)
    comment = models.CharField(verbose_name='备注', max_length=512, blank=True, null=True)