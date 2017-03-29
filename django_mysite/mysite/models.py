from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.urlresolvers import reverse


class UserManager(BaseUserManager):
	'''create user with email and password'''
	def create_user(self, email, username, password=None, **kwargs):
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email = UserManager.normalize_email(email),
			username = username,
			)
		user.set_password(password)
		if kwargs:
			if kwargs.get('sex', None): user.sex = kwargs['sex']
			if kwargs.get('is_active', None): user.is_active = kwargs['is_active']
			if kwargs.get('uid', None): user.uid = kwargs['uid']
			if kwargs.get('token', None): user.uid = kwargs['token']
			if kwargs.get('url', None): user.uid = kwargs['url']
			if kwargs.get('desc', None): user.uid = kwargs['desc']
			if kwargs.get('avatar', None): user.uid = kwargs['avatar']

		user.save(using = self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(email,
		password = password,
		username = username,
		)
		user.is_admin = True
		user.save(using = self._db)
		return user


class MyUser(AbstractBaseUser):
	'''extend user'''
	email = models.EmailField(verbose_name='Email address', max_length=255, unique=True, db_index=True)
	username = models.CharField(max_length=50, unique=True, db_index=True)		
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	sex = models.IntegerField(default=1)
	url = models.URLField(null=True)
	desc = models.CharField(max_length=2000, null=True)
	avatar = models.CharField(max_length = 500, null=True)
	token = models.CharField(max_length=500)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

	def __unicode__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property 
	def is_staff(self):
		return self.is_admin


	class Meta:
		db_table = 'user'


class CustomAuth(object):
	'''custuom user register'''
	def authenticate(self, email = None, password = None):
		try :
			user = MyUser.objects.get(email = email)
			if user.check_password(password):
				return user 
		except MyUser.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			user = MyUser.objects.get(pk = user_id)
			if user.is_active:
				return user 
			return None
		except MyUser.DoesNotExist:
			return None


class Answer(models.Model):
	answer_text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	counter = models.IntegerField(default=0)

	respondent = models.ForeignKey(MyUser)

	def __unicode__(self):
		return self.answer_text

	class Meta:
		verbose_name = 'answers'


class Question(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	publish = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	questioner = models.ForeignKey(MyUser)
	answers = models.ManyToManyField(Answer)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('qustion_detail', kwargs={'pk': self.pk})

	class Meta:
		verbose_name = 'Questions'
		ordering = ['-created']





	
			

				



