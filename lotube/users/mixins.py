from django.views.generic import View, ListView, CreateView

from .models import User


class UserListMixin(ListView):
    model = User
    template_name = 'users/user_list.html'

    def get_queryset(self):
        a = User.objects.all()
        print a[0].user.username
        print a
        return a
