# Generated by Django 4.2.1 on 2023-12-10 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='text',
        ),
    ]