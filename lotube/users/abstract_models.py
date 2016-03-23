from django.db import models
from django.contrib.auth.models import User
from django.db.models import GenericIPAddressField
from annoying.fields import AutoOneToOneField


class AbstractUser(models.Model):
    user = AutoOneToOneField(User, primary_key=True)
    ip_address = GenericIPAddressField()

    def __str__(self):
        return '{0}'.format(self.user)

    class Meta:
        abstract = True
