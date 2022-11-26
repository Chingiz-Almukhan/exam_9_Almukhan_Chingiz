from django.urls import reverse
from django.views.generic import CreateView

from gallery.forms import AddEditPictureForm
from gallery.models import Picture


class PictureAddView(CreateView):
    template_name = 'add_picture.html'
    model = Picture
    form_class = AddEditPictureForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('main')
