from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import UpdateView

from gallery.forms import AddEditPictureForm
from gallery.models import Picture
from gallery.views.base import CustomPassesTestMixin


class PictureUpdateView(CustomPassesTestMixin, UpdateView):
    model = Picture
    form_class = AddEditPictureForm
    template_name = 'edit_picture.html'

    def get_success_url(self):
        return reverse('picture_detail', kwargs={'pk': self.object.pk})
