from django.db import models
from django.contrib.auth.models import User
from django.db.models import GenericIPAddressField


class AbstractUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ip_address = GenericIPAddressField()

    class Meta:
        abstract = True
