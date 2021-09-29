from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=250)
    logo = models.CharField(max_length=250)

    def __str__(self):
        return "Team(%i) - %s" % (self.id, self.name)