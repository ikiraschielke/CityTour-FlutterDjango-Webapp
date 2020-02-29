import rest_framework
from rest_framework import serializers
from . models import Landmark, Media


class MediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Media
        fields = "__all__" #["landmark", 'name', "media"]

class LandmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Landmark
        fields = "__all__" #["landmark_id", "name", "longitude","latitude"]
