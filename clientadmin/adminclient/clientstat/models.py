# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from re import VERBOSE
from django.db import models
from django.shortcuts import reverse


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class Clients(models.Model):
    username = models.CharField(max_length=100)
    db_key = models.CharField(max_length=100)
    url_yandex = models.CharField(max_length=200)
    url_google = models.CharField(max_length=200)
    url_flamp = models.CharField(max_length=200)
    url_2gis = models.CharField(max_length=200)

    class Meta:
        managed = False
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        db_table = 'clients'
    
    def __str__(self):
        return f'Клиент {self.username}' 

    def get_absolute_url(self):
        return f"/clients/{self.db_key}"

    

class Comments(models.Model):
    comment_resurs = models.CharField(max_length=20)
    comment_number = models.IntegerField()
    status_coment = models.CharField(max_length=20)
    author_comment = models.CharField(max_length=50)
    text_comment = models.TextField()
    date_comment = models.CharField(max_length=10)
    mylike = models.IntegerField()
    dislike = models.IntegerField()
    comments_key = models.ForeignKey(Clients, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'comments'
    

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class Flamp(models.Model):
    date_parse = models.CharField(max_length=20)
    raiting = models.IntegerField()
    count_comments = models.IntegerField()
    flamp_key = models.ForeignKey(Clients, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'flamp'


class Google(models.Model):
    date_parse = models.CharField(max_length=20)
    raiting = models.IntegerField()
    count_comments = models.IntegerField()
    google_key = models.ForeignKey(Clients, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'google'


class Twogis(models.Model):
    date_parse = models.CharField(max_length=20)
    raiting = models.IntegerField()
    count_comments = models.IntegerField()
    gis_key = models.ForeignKey(Clients, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'twogis'


class Yandex(models.Model):
    name_model ='yandex'
    date_parse = models.CharField(max_length=20)
    raiting = models.CharField(max_length=5)
    count_comments = models.IntegerField()
    yandex_key = models.ForeignKey(Clients, models.DO_NOTHING)

    class Meta:
        verbose_name = 'Яндекс Карты'
        verbose_name_plural = 'Яндекс Карты'
        managed = False
        db_table = 'yandex'
        
        

    def __str__(self):
        return 'Яндекс Карты'
    
    def get_absolute_url(self):
        return reverse("comments", kwargs={'db_key':self.yandex_key.db_key,'resurs':self.name_model})

