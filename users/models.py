from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, User

from django.db.models.signals import post_save
from django.dispatch import receiver

# accounts/managers.py
from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    role_id = models.IntegerField(null=True)
    full_name = models.CharField(max_length=20, null=True)
    gender = models.IntegerField(default=1)
    dob = models.DateField(null=True, blank=True)
    about_me = models.CharField(max_length=100, null=True)
    fb_id = models.CharField(max_length=100, null=True)
    google_id = models.CharField(max_length=100, null=True)
    coinbase_client_id = models.TextField(max_length=100, null=True)
    mobile = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    photo = models.ImageField(default='default.png', upload_to='profile_image/%Y/%m/%d/', null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=20, null=True)
    country_id = models.IntegerField(null=True)
    postal_code = models.CharField(max_length=50, null=True)
    status = models.IntegerField(default=1)
    blocked_date = models.DateField(null=True, blank=True)
    created_at  = models.DateField(null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)
    remember_token = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
