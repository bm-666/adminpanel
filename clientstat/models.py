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
    url_yandex = models.CharField(max_length=200, default='url')
    url_google = models.CharField(max_length=200, default='url')
    url_flamp = models.CharField(max_length=200, default='url')
    url_2gis = models.CharField(max_length=200, default='url')

    class Meta:
        managed = False
        verbose_name = '????????????'
        verbose_name_plural = '??????????????'
        db_table = 'clients'
    
    def __str__(self):
        return f'???????????? {self.username}' 

    def get_absolute_url(self):
        return f"/clients/{self.db_key}"


class Comments(models.Model):
    choices = (
        ('yandex','????????????'),
        ('google','Google'),
        ('flamp','Flamp'),
        ('twogis','2Gis')

    )
    comment_resurs = models.CharField(max_length=20, blank=True, null=True,choices=choices, verbose_name="????????????")
    comment_number = models.IntegerField(blank=True, null=True, verbose_name="?????????? ??????????????????????")
    status_comment = models.CharField(max_length=20, blank=True, null=True, verbose_name="????????????")
    author_comment = models.CharField(max_length=50, blank=True, null=True, verbose_name="??????????")
    text_comment = models.TextField(blank=True, null=True,verbose_name="??????????")
    date_comment = models.CharField(max_length=10, blank=True, null=True, verbose_name="???????? ????????????????????")
    mylike = models.IntegerField(blank=True, null=True, verbose_name="????????")
    dislike = models.IntegerField(blank=True, null=True, verbose_name="??????????????")
    comment_stars = models.IntegerField(blank=True, null=True, verbose_name="????????????")
    date_delete = models.CharField(max_length=10, blank=True, null=True, verbose_name="???????? ????????????????")
    comment_key = models.ForeignKey(Clients, 
    models.DO_NOTHING, blank=True, null=True, verbose_name="????????????", )

    class Meta:
        managed = False
        db_table = 'comments'
        verbose_name = '??????????'
        verbose_name_plural = '????????????'
    
    def __str__(self) :
        return f'?????????? {self.comment_key}'

    def get_absolute_url(self):
        return reverse("date_comment", kwargs={"date_comment":self.date_comment})

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
    name_model = 'flamp'
    date_parse = models.CharField(max_length=20)
    raiting = models.CharField(max_length=5)
    count_comments = models.IntegerField()
    table_key = models.ForeignKey(Clients, models.DO_NOTHING)

    class Meta:
        verbose_name = 'Flamp'
        verbose_name_plural = 'Flamp'
        managed = False
        db_table = 'flamp'
    
    def __str__(self):
        return 'Flamp'
    
    def get_absolute_url(self):
        return reverse("comments", kwargs={'db_key':self.table_key.db_key,'resurs':self.name_model})


class Google(models.Model):
    name_model = 'google'
    date_parse = models.CharField(max_length=20)
    raiting = models.CharField(max_length=5)
    count_comments = models.IntegerField()
    table_key = models.ForeignKey(Clients, models.DO_NOTHING)

    class Meta:
        verbose_name = 'Google Maps'
        verbose_name_plural = 'Google Maps'
        managed = False
        db_table = 'google'
    
    def __str__(self):
        return 'Google Maps'
    
    def get_absolute_url(self):
        return reverse("comments", kwargs={'db_key':self.table_key.db_key,'resurs':self.name_model})


class Twogis(models.Model):
    name_model = 'twogis'
    date_parse = models.CharField(max_length=20)
    raiting = models.CharField(max_length=5)
    count_comments = models.IntegerField()
    table_key = models.ForeignKey(Clients, models.DO_NOTHING)

    class Meta:
        verbose_name = '2Gis'
        verbose_name_plural = '2Gis'
        managed = False
        db_table = 'twogis'
        
    def __str__(self):
        return '2Gis'
    
    def get_absolute_url(self):
        return reverse("comments", kwargs={'db_key':self.table_key.db_key,'resurs':self.name_model})


class Yandex(models.Model):
    name_model = 'yandex'
    date_parse = models.CharField(max_length=20)
    raiting = models.CharField(max_length=5)
    count_comments = models.IntegerField()
    table_key = models.ForeignKey(Clients, models.DO_NOTHING)

    class Meta:
        verbose_name = '???????????? ??????????'
        verbose_name_plural = '???????????? ??????????'
        managed = False
        db_table = 'yandex'
        
    def __str__(self):
        return '???????????? ??????????'
    
    def get_absolute_url(self):
        return reverse("comments", kwargs={'db_key':self.table_key.db_key,'resurs':self.name_model})
