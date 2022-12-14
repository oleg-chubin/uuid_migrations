# Generated by Django 4.0.5 on 2022-09-15 12:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core_base', '0003_participant_team_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='team',
        ),
        migrations.RemoveField(
            model_name='team',
            name='id',
        ),
        migrations.AlterField(
            model_name='team',
            name='uuid_hash',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
