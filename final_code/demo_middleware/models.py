from django.db import models

class newstats(models.Model):
  win = models.IntegerField()
  mac = models.IntegerField()
  iph = models.IntegerField()
  android = models.IntegerField()
  oth = models.IntegerField()

