from django.shortcuts import render, HttpResponse
from django.core.exceptions import *
#for file upload
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
# for filtering
from django_filters.rest_framework import DjangoFilterBackend
#from django_filters import rest_framework as filters
#misc imports
from rest_framework import viewsets,status, generics, filters


from . models import Landmark, Media
from . serializers import LandmarkSerializer, MediaSerializer
#from . filters import LandmarkFilter






#viewsets stick with them and not with the apiview makes routing also easier
# Create your views here.
class LandmarkView(viewsets.ModelViewSet):
    queryset = Landmark.objects.all()
    serializer_class = LandmarkSerializer
    
    #nach zahlen kann nur exzakt gefilter werden
    #mit searchfield und $ regex suche
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['landmark_id']



# ViewSets define the view behavior.
class MediaView(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['$name','$media', '$media_id']

########################################################
#get user input
def index(request):

    return render(request, 'radius_form.html')

def search(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            landmark = Landmark.objects.get(name = search_id)
            #landmark_serializer = LandmarkSerializer(landmark , many=True)
            #do something with user
            html = ("<H1>%s</H1>", landmark)
            return HttpResponse(html)
        except Landmark.DoesNotExist:
            return HttpResponse("no such landmark")  
    else:
        return render(request, 'form.html')

#function that actually calculates the radius for landmarks
def nearby_spots(request,longitude,latitude, radius, limit=50):
    """
    WITHOUT use of any external library, using raw MySQL and Haversine Formula
    http://en.wikipedia.org/wiki/Haversine_formula
    """
    radius = float(radius) / 1000.0

    query = """SELECT id, (6367*acos(cos(radians(%2f))
            *cos(radians(latitude))*cos(radians(longitude)-radians(%2f))
            +sin(radians(%2f))*sin(radians(latitude))))
            AS distance FROM webapp_landmark HAVING
            distance < %2f ORDER BY distance LIMIT 0, %d""" % (
        float(latitude),
        float(longitude),
        float(latitude),
        radius,
        limit
    )

    queryset = Landmark.objects.raw(query)
    serializer = LandmarkSerializer(queryset, many=True, context={'request': request})

    return queryset,Response(serializer.data)


def radius(request):
    if request.method == 'POST':
        longitude = request.POST.get('longfield', None)
        latitude = request.POST.get('latfield', None)
        radius = request.POST.get('radiusfield', None)
        try:
            #landmark = Landmark.objects.get(longitude=longitude,latitude=latitude) #, radius=radius
            #now call function for filtering and pass those parameters on
            filter_result, response = nearby_spots(request,longitude,latitude, radius)
            html = ("<H1>%s</H1>", filter_result)
            return HttpResponse(html)
        except Landmark.DoesNotExist:
            return HttpResponse("no matching results found")  
    else:
        return render(request, 'radius_form.html')




#########################################################

#simple view is enough 
class MediaUploadView(APIView):

    def get(self, request):
        media = Media.objects.all()

        media_serializer = MediaSerializer(media , many=True)
        return Response(media_serializer.data) 

    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      media_serializer = MediaSerializer(data=request.data)

      if media_serializer.is_valid():
          media_serializer.save()
          return Response(media_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(media_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

