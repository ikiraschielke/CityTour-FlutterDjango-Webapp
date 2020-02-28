from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from . models import Landmark, File
from . serializers import LandmarkSerializer, FileSerializer

# Create your views here.

class LandmarkList(APIView):

    def get(self, request):
        landmarkset = Landmark.objects.all()
        serializer = LandmarkSerializer(landmarkset,many=True)

        #returns json
        return Response(serializer.data)

    def post(self):
        pass


# for parsing raw file upload content
class FileUploadView(APIView):

    def get(self,request):
        fileset = File.objects.all()
        serializer = FileSerializer(fileset, many=True)

        return Response(serializer.data)


    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data) #, status=status.HTTP_201_CREATED
      else:
          return Response(file_serializer.errors) #, status=status.HTTP_400_BAD_REQUEST