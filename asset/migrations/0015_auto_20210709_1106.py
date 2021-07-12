# Generated by Django 3.2.5 on 2021-07-09 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0014_alter_table_new_asset_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='comment',
        ),
        migrations.AlterField(
            model_name='table',
            name='status',
            field=models.CharField(choices=[('库存', '库存'), ('出库', '出库'), ('报废', '报废'), ('损坏', '损坏'), ('出库审批', '出库审批'), ('报废审批', '报废审批')], default='库存', max_length=16, verbose_name='状态'),
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=512, verbose_name='备注')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='asset.table')),
            ],
        ),
    ]
