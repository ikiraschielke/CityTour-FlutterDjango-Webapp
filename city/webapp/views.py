from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Landmark
from . serializers import LandmarkSerializer

# Create your views here.

class LandmarkList(APIView):

    def get(self, request):
        landmarkset = Landmark.objects.all()
        serializer = LandmarkSerializer(landmarkset,many=True)

        #returns json
        return Response(serializer.data)

    def post(self):
        pass