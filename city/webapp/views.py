from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import *
#for file upload
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
# for filtering
# probably redundant as it is also in settings.py in DJANGO-REST
from django_filters.rest_framework import DjangoFilterBackend

#misc imports
from rest_framework import viewsets,status, generics, filters


from . models import Landmark, Media, TextBlock
from . serializers import LandmarkSerializer, MediaSerializer, TextBlockSerializer







#viewsets stick with them and not with the apiview makes routing also easier
# Create your views here.
class LandmarkView(viewsets.ModelViewSet):
    queryset = Landmark.objects.all()
    serializer_class = LandmarkSerializer
    
    #nach zahlen kann nur exzakt gefilter werden
    #mit searchfield und $ regex suche
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id']


# ViewSets define the view behavior.
class MediaView(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['$name','$media', '$id']

class TextBlockView(viewsets.ModelViewSet):
    queryset = TextBlock.objects.all()
    serializer_class = TextBlockSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['$header','$body']


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


# function wo which Django view url routes is linked to!
def radius(request):
    if request.method == 'POST':
        longitude = request.POST.get('longfield', None)
        latitude = request.POST.get('latfield', None)
        radius = request.POST.get('radiusfield', None)
        try:

            filter_result = nearby_spots(request,longitude,latitude, radius)
            #print(filter_result)
            serializer = LandmarkSerializer(filter_result, many=True, context={'request': request})
            html = (serializer.data)
            #print(html)

            #html = ("<H1>%s</H1>", filter_result[0],filter_result[1],filter_result[2])
            return HttpResponse(html)
            #JsonResponse(serializer.data, safe=False)
        except Landmark.DoesNotExist:
            return HttpResponse("no matching results found")  
    else:
        return render(request, 'radius_form.html')

#TEXTBLOCK
#########################################################
@csrf_exempt
def textblock_list(request):
    """
    List all textblock entries, or create a new text block entry.
    """
    if request.method == 'GET':
        textblocks = TextBlock.objects.all()
        serializer = TextBlockSerializer(textblocks, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TextBlockSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def textblock_detail(request, pk):
    """
    Retrieve, update or delete a textblock entry.
    """
    try:
        textblock = TextBlock.objects.get(pk=pk)
    except TextBlock.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TextBlockSerializer(textblock)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TextBlockSerializer(textblock, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        textblock.delete()
        return HttpResponse(status=204)
#########################################################

#Landmark
@csrf_exempt
def landmark_list(request):
    """
    List all textblock entries, or create a new landmark entry.
    """
    if request.method == 'GET':
        landmarks = Landmark.objects.all()
        serializer = LandmarkSerializer(landmarks, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LandmarkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def landmark_detail(request, pk):
    """
    Retrieve, update or delete a landmark entry.
    """
    try:
        landmark = Landmark.objects.get(pk=pk)
    except Landmark.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TextBlockSerializer(landmark)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LandmarkSerializer(landmark, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        landmark.delete()
        return HttpResponse(status=204)

###########################################################

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

