# Generated by Django 5.1.4 on 2024-12-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
