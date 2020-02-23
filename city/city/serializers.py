import rest_framework
from rest_framework import serializers
#from city.models import ExampleModel

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class LandmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Landmark
        fields = ["id", "name", "longitute", "latitude", "media"]

class MediaSerializer(serializers.HyperlinkedModelSerializer):

    #media array
    med_arr = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = Media
        fields = ["type", "value", "author", "created", "med_arr"]