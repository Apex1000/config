# Generated by Django 3.1.4 on 2021-06-06 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210603_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='manager',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]