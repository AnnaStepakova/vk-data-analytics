# Generated by Django 3.1.7 on 2021-04-04 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_vkuser_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vkuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='vkuser',
            name='last_name',
        ),
    ]