# Generated by Django 3.2.17 on 2023-04-17 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('person_name', models.TextField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Ioptc_region',
        ),
    ]