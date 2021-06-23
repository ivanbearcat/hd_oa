from django.contrib import admin
from .models import table
from django.http import HttpResponse
from openpyxl import Workbook
from django.contrib.admin.models import LogEntry


class ExportExcelMixin(object):
    def export_as_excel(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        field_verbose_names = [field.verbose_name for field in meta.fields]
        response = HttpResponse(content_type='application/msexcel')
        response['Content-Disposition'] = f'attachment; filename={meta}.xlsx'
        wb = Workbook()
        ws = wb.active
        ws.append(field_verbose_names)
        for obj in queryset:
            for _ in field_names:
                data = [f'{getattr(obj, field)}' for field in field_names]
            ws.append(data)
        wb.save(response)
        return response
    export_as_excel.short_description = '导出Excel'



# Register your models here.
@admin.register(table)
class tableAdmin(admin.ModelAdmin, ExportExcelMixin):
    list_display = ('server_ip', 'ssh_port', 'user', 'password', 'model', 'sn', 'cpu', 'memory', 'disk', 'os',
                    'deployment_plan', 'doployment_mod', 'remote_card_ip', 'remote_card_user', 'remote_card_password',
                    'organization', 'old_asset_number', 'new_asset_number', 'owner', 'owner_department', 'is_use',
                    'cost_center', 'checker', 'create_time', 'location', 'comment')

    # list_display_links = ('server_ip',)

    search_fields = ('server_ip', 'owner', 'owner_department')

    date_hierarchy = 'create_time'

    list_per_page = 10
    # list_filter = ('server_ip', 'ssh_port')
    actions = ['export_as_excel']



@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['action_time', 'object_repr', 'object_id', 'content_type_id', 'action_flag', 'user','change_message']

    date_hierarchy = 'action_time'

    list_per_page = 15