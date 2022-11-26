from django.urls import path

from gallery.views.add_picture_view import PictureAddView
from gallery.views.base import PostView
from gallery.views.picture_delete_view import PictureDeleteView
from gallery.views.picture_detail_view import PictureDetailView
from gallery.views.picture_edit_view import PictureUpdateView

urlpatterns = [
    path("", PostView.as_view(), name='main'),
    path('add/picture', PictureAddView.as_view(), name='add_picture'),
    path('picture/detail/<int:pk>', PictureDetailView.as_view(), name='picture_detail'),
    path('picture/delete/<int:pk>', PictureDeleteView.as_view(), name='delete_picture'),
    path('picture/edit/<int:pk>', PictureUpdateView.as_view(), name='edit_picture')
]
