from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, \
    UpdateModelMixin

from .models import User
from .serializers import UserSerializer
from core.api_utils import IsOwnerOrReadOnlyUser


class UserAPIView(GenericViewSet,
                  ListModelMixin,
                  RetrieveModelMixin,
                  UpdateModelMixin):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyUser]
    filter_fields = ('id', 'username',)
