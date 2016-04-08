from django.test import TestCase

from users.models import User


class TestDefaultUser(TestCase):

    def setUp(self):
        self.user = User()

    def test_is_not_staff(self):
        self.assertFalse(self.user.is_staff)
