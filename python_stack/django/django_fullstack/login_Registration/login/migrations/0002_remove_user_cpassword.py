# Generated by Django 2.2.4 on 2021-05-29 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cpassword',
        ),
    ]
