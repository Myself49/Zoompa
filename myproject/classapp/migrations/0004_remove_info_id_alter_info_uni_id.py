# Generated by Django 5.1.4 on 2024-12-10 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0003_remove_info_nic_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='id',
        ),
        migrations.AlterField(
            model_name='info',
            name='uni_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
