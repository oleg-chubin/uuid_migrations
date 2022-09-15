# Generated by Django 4.0.5 on 2022-09-15 11:22

from django.db import migrations, models
from django.db.models import F


def forwards_func(apps, schema_editor):
    """
    We can use raw SQL to improve performance of this method
    currently this method works for me
    """
    Team = apps.get_model("core_base", "Team")
    for team in Team.objects.all():
        team.participant_set.update(team_uuid=team.uuid_hash)


def reverse_func(apps, schema_editor):
    Participant = apps.get_model("core_base", "Participant")
    Participant.objects.update(uuid_hash=None)


class Migration(migrations.Migration):

    dependencies = [
        ('core_base', '0002_team_uuid_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='team_uuid',
            field=models.UUIDField(null=True),
        ),
        migrations.RunPython(forwards_func, reverse_func),
        migrations.AlterField(
            model_name='participant',
            name='team_uuid',
            field=models.UUIDField(null=False),
        ),
    ]