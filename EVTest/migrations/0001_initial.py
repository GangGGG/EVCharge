# Generated by Django 2.2.1 on 2019-08-19 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptno', models.AutoField(primary_key=True, serialize=False)),
                ('dname', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'dept',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Electricprice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identify', models.IntegerField(blank=True, db_column='ID', null=True)),
                ('time', models.FloatField(blank=True, db_column='Time', null=True)),
                ('soc', models.FloatField(blank=True, db_column='SOC', null=True)),
            ],
            options={
                'db_table': 'electricprice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.AutoField(primary_key=True, serialize=False)),
                ('ename', models.CharField(blank=True, max_length=50, null=True)),
                ('sal', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'emp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Emptest',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(blank=True, max_length=50, null=True)),
                ('deptno', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'emptest',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Husband',
            fields=[
                ('hid', models.AutoField(primary_key=True, serialize=False)),
                ('hname', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'husband',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stateofcharge',
            fields=[
                ('userid', models.CharField(db_column='UserID', max_length=32, primary_key=True, serialize=False)),
                ('soc', models.FloatField(blank=True, db_column='SOC', null=True)),
                ('times', models.CharField(blank=True, db_column='Times', max_length=32, null=True)),
                ('flag', models.IntegerField(blank=True, db_column='Flag', null=True)),
            ],
            options={
                'db_table': 'stateofcharge',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StuTea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'stu_tea',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TabBin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(blank=True, max_length=100, null=True)),
                ('data', models.TextField(blank=True, db_column='DATA', null=True)),
            ],
            options={
                'db_table': 'tab_bin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbStu',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('agender', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'tb_stu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbTest',
            fields=[
                ('x', models.AutoField(primary_key=True, serialize=False)),
                ('y', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tb_test',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('tname', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'teacher',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TStu',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(blank=True, max_length=20, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 't_stu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 't_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wife',
            fields=[
                ('wid', models.ForeignKey(db_column='wid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='EVTest.Husband')),
                ('wname', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'wife',
                'managed': False,
            },
        ),
    ]
