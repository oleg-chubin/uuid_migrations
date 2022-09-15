import uuid

from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=120)
    uuid_hash = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)


class Participant(models.Model):
    name = models.CharField(max_length=120)
    team_uuid = models.UUIDField()
