import rest_framework
from rest_framework import serializers
from . models import Landmark, Media, TextBlock


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__" #["landmark", 'name', "media"]


class LandmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landmark
        fields = "__all__" #["landmark_id", "name", "longitude","latitude"]


# ModelSerializerclass have default implementation for create() and update()
class TextBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextBlock
        fields = ['header','body']