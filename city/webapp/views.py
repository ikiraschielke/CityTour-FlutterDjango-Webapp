from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

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
def nearby_spots(request,longitude,latitude, radius):
    """
    WITHOUT use of any external library, using raw MySQL and Haversine Formula
    http://en.wikipedia.org/wiki/Haversine_formula
    """
    radius = float(radius) 

    query = """SELECT id, (6367*
                            acos(
                                cos(radians(%8f))*
                                cos(radians(latitude))*
                                cos(radians(longitude)-
                                radians(%8f))+
                                sin(radians(%8f))*
                                sin(radians(latitude))
                                )
                            )
            AS distance FROM webapp_landmark HAVING
            distance < %2f ORDER BY distance ASC""" % (
        float(latitude),
        float(longitude),
        float(latitude),
        radius
    )

    queryset = Landmark.objects.raw(query)
    #print(type(queryset)) <class 'django.db.models.query.RawQuerySet'>
    #print(queryset) #query mit werten ausgefüllt
    #for p in queryset:
    #    print(type(p)) #<class 'webapp.models.Landmark'>
    #    print(p)


    serializer = LandmarkSerializer(queryset, many=True, context={'request': request})
    print(serializer.data)


    #just return the list to the radius function but render in radius
    return  queryset #JsonResponse(serializer.data, safe=False)


def radius(request):
    if request.method == 'POST':
        longitude = request.POST.get('longfield', None)
        latitude = request.POST.get('latfield', None)
        radius = request.POST.get('radiusfield', None)
        try:

            filter_result = nearby_spots(request,longitude,latitude, radius)
            serializer = LandmarkSerializer(filter_result, many=True, context={'request': request})
            html = (serializer.data)

            #html = ("<H1>%s</H1>", filter_result[0],filter_result[1],filter_result[2])
            return HttpResponse(html)
            #JsonResponse(serializer.data, safe=False)
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

