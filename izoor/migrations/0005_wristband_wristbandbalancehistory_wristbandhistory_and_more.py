# Generated by Django 4.0.7 on 2022-09-28 11:48

import api.mssql_uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('izoor', '0004_alter_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wristband',
            fields=[
                ('id', models.CharField(db_column='Wrist_NUM', default=None, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('balance', models.DecimalField(db_column='Top_up_rest', decimal_places=4, max_digits=19)),
            ],
            options={
                'db_table': 'Wristbands',
                'ordering': ['id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WristbandBalanceHistory',
            fields=[
                ('slug', api.mssql_uuid.MssqlUUID(db_column='WristDepoId', default=None, editable=False, primary_key=True, serialize=False)),
                ('number', models.CharField(db_column='Wrist_NUM', default=None, editable=False, max_length=10)),
                ('type', models.CharField(db_column='OperationType', default='TOP', max_length=3)),
                ('sign', models.IntegerField(db_column='OperationSign')),
                ('amount', models.DecimalField(db_column='OperationSumm', decimal_places=4, max_digits=19)),
                ('bill_number', models.CharField(db_column='RelDocumentNum', max_length=3)),
                ('time', models.DateTimeField(auto_now_add=True, db_column='OperationDate')),
                ('description', models.CharField(db_column='OperationDesc', max_length=3)),
                ('accept', models.BooleanField(db_column='OperationAccepted', default=True)),
            ],
            options={
                'db_table': 'WristDeposite',
                'ordering': ['-time'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WristbandHistory',
            fields=[
                ('slug', api.mssql_uuid.MssqlUUID(db_column='WristEventId', default=None, editable=False, primary_key=True, serialize=False)),
                ('number', models.CharField(db_column='Wrist_NUM', default=None, editable=False, max_length=10)),
                ('time', models.DateTimeField(auto_now_add=True, db_column='WristEventDate')),
                ('type', models.CharField(db_column='EventType', max_length=6)),
                ('place', models.CharField(db_column='PLaceId', max_length=16)),
                ('description', models.CharField(blank=True, db_column='Comment', max_length=50, null=True)),
            ],
            options={
                'db_table': 'WristEvents',
                'ordering': ['-time'],
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Wristbands',
        ),
    ]