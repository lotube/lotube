import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models
from django.db.models import GenericIPAddressField
from django.utils.timezone import utc

from core.models import LowerCaseCharField
from core.validators import Common
from . import constants


class AbstractUser(AbstractBaseUser):
    """
    Remember that password and last_login are inherited from AbstractBaseUser.
    """
    username = LowerCaseCharField(max_length=50, db_index=True, unique=True,
                                  validators=[
                                      Common.alphanumeric(),
                                      Common.min_length(5),
                                      Common.starts_with_letter(),
                                  ])
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=300, blank=True, default='')
    last_name = models.CharField(max_length=300, blank=True, default='')
    ip_address = GenericIPAddressField(null=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    @property
    def is_active(self):
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        last_seen = self.date_joined if self.last_login is None else \
            max(self.date_joined, self.last_login)
        return (now - last_seen).days <= constants.ACTIVE_DAYS

    @property
    def is_superuser(self):
        return self.is_staff

    def get_full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return '{0}'.format(self.username)

    class Meta:
        abstract = True
