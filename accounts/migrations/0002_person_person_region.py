# Generated by Django 3.2.17 on 2023-04-17 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_reg'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_region',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.reg'),
        ),
    ]
