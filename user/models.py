from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator



class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, validators=[RegexValidator(r'^[\w.@+-]+$')])
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    REQUIRED_FIELDS = ['email', 'phone_number']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username