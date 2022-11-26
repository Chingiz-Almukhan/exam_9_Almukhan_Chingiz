from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from django.views.generic import TemplateView, DetailView, CreateView

from accounts.forms import LoginForm, CustomUserCreationForm
from gallery.models import Picture


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('main')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('username')
        user = authenticate(request, username=email, password=password)
        if not user:
            return redirect('main')
        login(request, user)
        return redirect('main')


def logout_view(request):
    logout(request)
    return redirect('main')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
        context = {}
        context['form'] = form
        return self.render_to_response(context)


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = "profile.html"
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Picture.objects.filter(author=user)
        # context['vacancy'] = Vacancy.objects.filter(author=user).order_by('-updated_at')
        # context['change_form'] = UserChangeForm(instance=self.object)
        return context
