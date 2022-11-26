from django.views.generic import DeleteView

from gallery.models import Picture
from gallery.views.base import CustomPassesTestMixin


class PictureDeleteView(CustomPassesTestMixin,DeleteView):
    model = Picture
    success_url = "/"
