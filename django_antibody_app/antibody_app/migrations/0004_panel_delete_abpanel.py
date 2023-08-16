# Generated by Django 4.2.3 on 2023-08-16 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antibody_app', '0003_delete_zzantigenreactivity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('panel_id', models.AutoField(primary_key=True, serialize=False)),
                ('panel_name', models.CharField(max_length=45)),
                ('owner', models.CharField(max_length=10)),
                ('is_public', models.IntegerField()),
                ('application', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'ab_panel',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='AbPanel',
        ),
    ]
