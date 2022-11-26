from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView

from gallery.models import Picture


class PostView(ListView):
    template_name = 'index.html'
    model = Picture
    context_object_name = 'pictures'


class CustomPassesTestMixin(UserPassesTestMixin):

    def test_func(self):
        self.object = self.get_object()
        return self.request.user == self.object.author or self.request.user.is_superuser
