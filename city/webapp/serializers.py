import rest_framework
from rest_framework import serializers
from . models import Landmark, Media, TextBlock

"""
 ModelSerializerclass have default implementation for create() and update()

"""

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        #"__all__" returns all fields of Class Instance: ["id", "name", "media"]
        fields = "__all__"


class TextBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextBlock
        fields = "__all__"


class LandmarkSerializer(serializers.ModelSerializer):

    #media = MediaSerializer(many=True)
    #text = TextBlockSerializer(many=True)
    #output: put_ser  LandmarkSerializer(data={'media': [7, 3], 'text': [3, 6], 'name': 'just über json', 'desc': 'cbeijd', 'longitude': 83.0, 'latitude': 2.3}):media ser und text ser

    class Meta:
        model = Landmark
        fields = "__all__"

