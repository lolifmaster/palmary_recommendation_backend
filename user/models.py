from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(username, email, password, **extra_fields)

    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError(_('The username must be set'))
        if not email:
            raise ValueError(_('The email must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username.capitalize(), email=email, **extra_fields)
        user.set_password(password)

        user.save()
        return user


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=150, validators=[RegexValidator(r'[a-zA-Z][\w.-]{0,24}$',
                                                                           _('username must be start with character following by (characters, digits, /_/-) max length is 25.'))])
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.username
