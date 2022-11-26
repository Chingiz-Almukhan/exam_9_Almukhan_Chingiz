from django.views.generic import ListView

from gallery.models import Picture


class PostView(ListView):
    template_name = 'index.html'
    model = Picture
    context_object_name = 'pictures'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        # user = self.request.user
        # posts = Post.objects.filter(author__in=subscribers).order_by('-created_at')
        # context['posts'] = posts
        # context['form'] = SearchForm()
        # context['comment_form'] = AddCommentForm()
        return context