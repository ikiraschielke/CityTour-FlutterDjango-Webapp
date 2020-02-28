from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.



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
        #db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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

###########################################

class Landmark(models.Model):
    landmark_id = models.IntegerField(primary_key=True)
    name    = models.CharField(max_length=200)
    media   = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()
    file = models.FileField(null=True)

    def __str__(self):     
        return "{} - {} loc: {}-{}".format(self.landmark_id, self.name,self.longitude, self.latitude)

"""
Files uploaded to FileField are not saved in the database but in the file system of your server. 
In the database it's the fields are represented by a VARCHAR containing the reference to the file.
"""

class File(models.Model):
    name    = models.CharField(max_length=200)
    file = models.FileField()

    def __str__(self):
        return "{} - {}".format(self.name, self.file.name)

#TODO LATER IMAGEFIELD

# Create your models here.
"""
class User(models.Model):
	user_id		= models.IntegerField(primary_key=True)
	firstname	= models.CharField(max_length=200)
	lastname    = models.CharField(max_length=200)
	email		= models.CharField(unique=True, max_length=200)
	
	def __str__(self):     
		return self.email

	#class Meta:     
	#	managed = False       
	#	db_table = 'users'



	
class Admin(models.Model):
	admin_id	= models.IntegerField(primary_key=True)
	firstname	= models.CharField(max_length=200)
	lastname    = models.CharField(max_length=200)
	email		= models.CharField(unique=True, max_length=200)
	
	def __str__(self):
		return self.email

	#class Meta:
	#	managed = False    
	#	db_table = 'admins' 



class Media(models.Model):
	media_id = models.IntegerField(primary_key=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='medias')


# one user can have multiple tours
# one medium can belong to multiple tours
class Tour(models.Model):
	tour_id =  models.IntegerField(primary_key=True)
	name = models.CharField(unique=True, max_length=40)
	user_id = models.ForeignKey(User, db_column='user_id', on_delete=models.CASCADE, related_name = 'users')
	media_id = models.ForeignKey(Media,db_column='media_id',on_delete=models.CASCADE, related_name='tours')
	description = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	class Meta:
		managed = False
		#db_table = 'tours'
		#unique_together = (('user_id','media_id'))
		#but instead
		#which unique sets do we have within one tour?!
		#constraints = [
        #    models.UniqueConstraint(fields=['user_id', 'media_id'], name='unique_tour')
        #]
	"""
