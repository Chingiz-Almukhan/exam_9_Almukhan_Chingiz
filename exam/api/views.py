
from typing import Any

from django import http
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from gallery.models import Picture


class PictureFavoriteView(LoginRequiredMixin, View):
    picture_object = None

    def dispatch(self, request: http.HttpRequest, *args: Any, **kwargs: Any):
        self.picture_object = get_object_or_404(Picture, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user_add_to_favorite = self.picture_object.user_favorite.values_list('id', flat=True)
        data = {}

        if request.user.pk in user_add_to_favorite:
            self.remove_favorite()
            data['result'] = 'deleted'
        else:
            self.add_favorite()
            data['result'] = 'added'
        return JsonResponse(data)

    def add_favorite(self):
        self.picture_object.user_favorite.add(self.request.user)

    def remove_favorite(self):
        self.picture_object.user_favorite.remove(self.request.user)








