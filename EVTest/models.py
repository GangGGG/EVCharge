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


class Electricprice(models.Model):
    identify = models.IntegerField(primary_key=True, db_column='ID', blank=True)  # Field name made lowercase.
    time = models.FloatField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    soc = models.FloatField(db_column='SOC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'electricprice'


class EvtpUser(models.Model):
    id = models.CharField(primary_key=True, max_length=32, blank=True)
    ev_id = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    home_position_id = models.CharField(max_length=32, blank=True, null=True)
    company_position_id = models.CharField(max_length=32, blank=True, null=True)
    other_position_id = models.CharField(max_length=2000, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    qq = models.CharField(max_length=100, blank=True, null=True)
    telnumber = models.CharField(max_length=100, blank=True, null=True)
    createdate = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=10, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    account = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evtp_user'
