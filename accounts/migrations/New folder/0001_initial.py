# Generated by Django 3.2.17 on 2023-04-16 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ioptc_region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('region_name', models.TextField(max_length=200)),
            ],
        ),
    ]