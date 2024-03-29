# Generated by Django 3.2.17 on 2023-04-26 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_reg'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tanktype1',
            options={'managed': True},
        ),
        migrations.CreateModel(
            name='Tank_calibration_excel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tank_name', models.TextField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('Calibration_excel', models.FileField(upload_to='calibration_excel/')),
                ('metric_or_imperial', models.CharField(choices=[('Metric', 'Metric'), ('Imperial', 'Imperial')], default='Metric', max_length=8)),
                ('Calibration_data', models.BooleanField(default=True)),
                ('type', models.TextField(choices=[('0', 'خط لوله '), ('2', 'پخش '), ('3', 'الوده'), ('4', 'پالایشگاه'), ('5', 'بندر صادرات'), ('6', 'پتروشیمی'), ('7', 'نیروگاه')], default=0, max_length=2)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('more_information', models.TextField(null=True)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.oilproducts')),
                ('region_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.reg')),
                ('station_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.station')),
                ('tank_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.tank')),
            ],
        ),
    ]
