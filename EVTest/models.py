# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Dept(models.Model):
    deptno = models.AutoField(primary_key=True)
    dname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dept'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Electricprice(models.Model):
    identify = models.IntegerField(db_column='ID', blank=True, null=True)
    time = models.FloatField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    soc = models.FloatField(db_column='SOC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'electricprice'


class Emp(models.Model):
    empno = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=50, blank=True, null=True)
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='deptno', blank=True, null=True)
    sal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp'


class Emptest(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=50, blank=True, null=True)
    deptno = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emptest'


class Husband(models.Model):
    hid = models.AutoField(primary_key=True)
    hname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'husband'

class Stateofcharge(models.Model):
    uuid = models.CharField(db_column='UUID', max_length=64)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=64)  # Field name made lowercase.
    soc = models.FloatField(db_column='SOC', blank=True, null=True)  # Field name made lowercase.
    times = models.CharField(db_column='Times', max_length=32, blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stateofcharge'


class StuTea(models.Model):
    sid = models.ForeignKey('Student', models.DO_NOTHING, db_column='sid', blank=True, null=True)
    tid = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='tid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stu_tea'


class Student(models.Model):
    sid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class TStu(models.Model):
    sid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stu'


class TUser(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'


class TabBin(models.Model):
    filename = models.CharField(max_length=100, blank=True, null=True)
    data = models.TextField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tab_bin'


class TbStu(models.Model):
    number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    agender = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_stu'


class TbTest(models.Model):
    x = models.AutoField(primary_key=True)
    y = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_test'


class Teacher(models.Model):
    tid = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacher'


class Wife(models.Model):
    wid = models.ForeignKey(Husband, models.DO_NOTHING, db_column='wid', primary_key=True)
    wname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wife'
