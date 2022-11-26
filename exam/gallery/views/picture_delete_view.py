from django.views.generic import DeleteView

from gallery.models import Picture


class PictureDeleteView(DeleteView):
    model = Picture
    success_url = "/"
