# Generated by Django 2.2.8 on 2020-04-16 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_auto_20200416_1500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_id',
            new_name='email',
        ),
    ]
