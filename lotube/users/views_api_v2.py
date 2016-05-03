from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, \
    UpdateModelMixin

from .models import User
from .serializers import UserSerializer


class UserAPIView(GenericViewSet,
                  ListModelMixin,
                  RetrieveModelMixin,
                  UpdateModelMixin):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
