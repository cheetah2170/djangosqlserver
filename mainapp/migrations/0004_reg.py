# Generated by Django 3.2.17 on 2023-04-16 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_station_region_relation'),
    ]

    operations = [
        migrations.CreateModel(
            name='REG',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=200)),
            ],
        ),
    ]
