# Generated by Django 3.2.17 on 2023-04-17 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('person_name', models.TextField(max_length=200)),
            ],
        ),
    ]