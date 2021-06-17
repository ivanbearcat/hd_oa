#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json
from asset.models import table as _table


@login_required
def table(request):
    return render(request, 'asset/table.html',{'user': request.user.username,
                                               'path1': 'asset',
                                               'path2': 'asset_table',
                                               'page_name1': '资产管理',
                                               'page_name2': '资产表',})



@login_required
def table_data(request):
    orm = _table.objects.all()
    tableData = []
    for i in orm:
        tableData.append({
            'id': i.id,
            'server_ip': i.server_ip,
            'ssh_port': str(i.ssh_port),
            'password': i.password,
            'model': i.model,
            'sn': i.sn,
            'cpu': i.cpu,
            'memory': i.memory,
            'disk': i.disk,
            'os': i.os,
            'deployment_plan': i.deployment_plan,
            'doployment_mod': i.doployment_mod,
            'remote_card_ip': i.remote_card_ip,
            'remote_card_user': i.remote_card_user,
            'remote_card_password': i.remote_card_password,
            'organization': i.organization,
            'old_asset_number': i.old_asset_number,
            'new_asset_number': i.new_asset_number,
            'owner': i.owner,
            'owner_department': i.owner_department,
            'is_use': i.is_use,
            'cost_center': i.cost_center,
            'checker': i.checker,
            'create_time': str(i.create_time).split('+')[0],
        })
    return HttpResponse(json.dumps({'code': -1, 'tableData': tableData}), content_type="application/json")