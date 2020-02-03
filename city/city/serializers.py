import rest_framework
#from rest_framework import serializers
from city.models import ExampleModel

class ExampleModelSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = ('firstname', 'lastname')