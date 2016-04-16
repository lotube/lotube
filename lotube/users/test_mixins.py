from django.http.response import Http404
from django.test import TestCase, RequestFactory

from users.mixins import UserDetailMixin
from users.models import User


class TestUserDetailsMixin(TestCase):

    class DummyView(UserDetailMixin):
        template_name = 'any_template.html'

    def setUp(self):
        super(TestUserDetailsMixin, self).setUp()

    def test_view_returns_404_with_a_non_existing_user(self):
        kwargs = {'username': 'non_existing_user'}
        request = RequestFactory().get('/any-user-detail')
        with self.assertRaises(Http404):
            self.DummyView.as_view()(request, **kwargs)

    def test_view_returns_user_if_it_exists(self):
        default = User(username='default', email='default@example.com')
        default.save()
        kwargs = {'username': 'default'}
        request = RequestFactory().get('/any-user-detail')
        response = self.DummyView.as_view()(request, **kwargs)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['object'], default)
        self.assertEqual(response.context_data['user'], default)
