from django import forms

from gallery.models import Picture


class AddEditPictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['description', 'image']
