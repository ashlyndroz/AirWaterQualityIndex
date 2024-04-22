from django.db import models


class PMSData(models.Model):
    pm_1_0 = models.FloatField()
    pm_2_5 = models.FloatField()
    pm_10_0 = models.FloatField()

class MQ7Data(models.Model):
    mq7_data = models.FloatField()

class GPSData(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()

class PhSensor(models.Model):
    ph_data = models.FloatField()

class TempSensor(models.Model):
    temp = models.FloatField()

class TDSSensor(models.Model):
    tds = models.FloatField()
