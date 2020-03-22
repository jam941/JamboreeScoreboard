from django.db import models

# Create your models here.


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
    """
    A scout
    """


class Score(models.Model):
    """
    A score
    """
