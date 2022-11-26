from django.urls import path

from api.views import PictureFavoriteView

urlpatterns = [
    path("add_to_favorite/<int:pk>", PictureFavoriteView.as_view(), name='add_to_favorite'),

]
