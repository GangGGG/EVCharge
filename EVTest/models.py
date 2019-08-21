# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Stateofcharge(models.Model):
    uuid = models.CharField(db_column='UUID', max_length=64)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=64)  # Field name made lowercase.
    soc = models.FloatField(db_column='SOC', blank=True, null=True)  # Field name made lowercase.
    times = models.CharField(db_column='Times', max_length=32, blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    money = models.CharField(db_column='Money', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stateofcharge'