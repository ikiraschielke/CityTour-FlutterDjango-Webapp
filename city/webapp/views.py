from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import viewsets,status
from . models import Landmark, Media
from . serializers import LandmarkSerializer, MediaSerializer

# Create your views here.
class LandmarkView(viewsets.ModelViewSet):
    queryset = Landmark.objects.all()
    serializer_class = LandmarkSerializer

# ViewSets define the view behavior.
class MediaView(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

"""
class LandmarkList(APIView):

    def get(self, request):
        landmarkset = Landmark.objects.all()
        serializer = LandmarkSerializer(landmarkset,many=True)

        #returns json
        return Response(serializer.data)

    def post(self):
        pass


# for parsing raw media upload content
class MediaUploadView(APIView):

    def get(self,request):
        mediaset = Media.objects.all()
        serializer = MediaSerializer(mediaset,many=True, context={'request': request})

        return Response(serializer.data)
    
    def post(self):
        pass


    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      media_serializer = MediaSerializer(data=request.data)

      if media_serializer.is_valid():
          media_serializer.save()
          return Response(media_serializer.data) #, status=status.HTTP_201_CREATED
      else:
          return Response(media_serializer.errors) #, status=status.HTTP_400_BAD_REQUEST
"""