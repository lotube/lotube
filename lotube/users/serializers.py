from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField

from users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    href = HyperlinkedIdentityField(view_name='api_v2:users-detail')

    class Meta:
        model = User
        fields = ('id', 'href', 'username', 'first_name', 'last_name', 'date_joined',
                  'last_login', 'is_staff', 'is_active')
