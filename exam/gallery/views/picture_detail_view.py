from django.views.generic import DetailView

from gallery.models import Picture


class PictureDetailView(DetailView):
    model = Picture
    template_name = 'picture_detail.html'
    context_object_name = 'picture'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
