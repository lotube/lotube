from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView

from users.forms import UserCreationForm, UserUpdateForm
from .mixins import UserListMixin, UserDetailMixin, UserDeleteMixin, \
    UserUpdateMixin


class UserList(UserListMixin):
    template_name = 'users/user_list.html'


class UserDetail(UserDetailMixin):
    template_name = 'users/user_detail.html'


class UserUpdate(UserUpdateMixin):
    template_name = 'users/update.html'
    form_class = UserUpdateForm

    def get_success_url(self):
        return reverse('web:users:update', args=[self.kwargs['username']])


class UserDelete(UserDeleteMixin):
    success_url = '/'
    template_name = 'users/delete.html'


class RegisterView(CreateView):
    template_name = 'users/signup.html'
    form_class = UserCreationForm
    success_url = '/'


class LoginView(TemplateView):
    """
    Login View, custom form handling related with a custom .html template
    Fields are email and password, both gathered by POST.
    Errors list like {{ errors }}
    """
    template_name = 'users/login.html'
    success_url = '/'

    def __init__(self, **kwargs):
        super(LoginView, self).__init__(**kwargs)
        self.errors = []

    def get(self, request, *args, **kwargs):
        # TODO redirect to success url if already-logged-in
        return super(LoginView, self).get(request, args, kwargs)

    def post(self, request, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            self.errors.append('Credentials are invalid')
        else:
            login(request, user)
            return redirect(self.success_url)
        return super(LoginView, self).get(request, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['errors'] = self.errors
        return context


class LogoutView(RedirectView):
    """
    Logout view, will redirect to login view regardless of user having been
    authenticated or not.
    """
    pattern_name = 'web:users:login'

    def get_redirect_url(self, **kwargs):
        logout(self.request)
        return super(LogoutView, self).get_redirect_url(**kwargs)
