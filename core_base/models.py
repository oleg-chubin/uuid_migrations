from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=120)


class Participant(models.Model):
    name = models.CharField(max_length=120)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
