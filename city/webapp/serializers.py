import rest_framework
from rest_framework import serializers
from . models import Landmark

class LandmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Landmark
        fields = ["landmark_id", "name", "n_media"]
        #or in fancy
        #fields = '__all__'


"""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']



class MediaSerializer(serializers.HyperlinkedModelSerializer):

    #media array
    med_arr = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = Media
        fields = ["type", "value", "author", "created", "med_arr"]
"""