"""
TODO add announcements, station
"""
from django.db import models


# Create your models here.

class Score(models.Model):
    score = models.IntegerField()
    submit_date = models.DateTimeField(auto_now_add=True)
    submit_user = models.CharField(max_length=128)
    comment = models.CharField(max_length=256)
    scout = models.ForeignKey('backend.Scout', null=True, on_delete=models.CASCADE)
    patrol = models.ForeignKey('backend.Patrol', null=True, on_delete=models.CASCADE)


class Troop(models.Model):
    """
    A Troop
    """
    number = models.IntegerField()
    district = models.CharField(max_length=128)
    council = models.CharField(max_length=128)
    scoutmaster = models.CharField(max_length=128)
    emergency_contact_num = models.CharField(max_length=16)

    def __str__(self):
        return f"Troop {self.number}"


class Patrol(models.Model):
    """
    A patrol
    """
    name = models.CharField(max_length=128)
    troop = models.ForeignKey('backend.Troop', on_delete=models.CASCADE)

    def __str__(self):
        return f"Patrol {self.name} - {self.troop.number}"


class Scout(models.Model):
    name = models.CharField(max_length=128)
    patrol = models.ForeignKey('backend.Patrol', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Station(models.Model):
    name = models.CharField(max_length=128)
