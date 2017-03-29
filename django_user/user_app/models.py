from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
# Create your models here.


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password,is_staff,**extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,is_staff=is_staff,
                            last_login=now,
                            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email,password, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True,
                                 **extra_fields)


class MyUser(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(verbose_name='email',blank=True,unique=True)
    is_staff = models.BooleanField('staff status', default=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        # full_name = '%s %s' % (self.first_name, self.last_name)
        return self.email

    def get_short_name(self):
        "Returns the short name for the user."
        return self.email
    # REQUIRED_FIELDS = ['email']