# Generated by Django 2.0.7 on 2019-06-26 08:39

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('oneid_meta', '0033_invitation'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='invitation',
            managers=[
                ('active_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]