# Generated by Django 4.2 on 2023-04-23 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='topic',
        ),
    ]
