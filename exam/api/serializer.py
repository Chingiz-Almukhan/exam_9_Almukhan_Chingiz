from rest_framework import serializers

from accounts.models import Account
from gallery.models import Picture


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id',)


class AddToFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('favorite_pictures',)
