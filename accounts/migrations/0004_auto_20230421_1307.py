# Generated by Django 3.2.17 on 2023-04-21 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20230417_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='can_change_data',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='more_information',
            field=models.TextField(default=None, null=True),
        ),
    ]
