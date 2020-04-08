from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import *
#for file upload
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.response import Response

# for filtering
from django_filters.rest_framework import DjangoFilterBackend

#misc imports
from rest_framework import viewsets,status , filters


from . models import Landmark, Media, TextBlock
from . serializers import LandmarkSerializer, MediaSerializer, TextBlockSerializer


from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.decorators import action, parser_classes
from django.core import serializers



# ViewSets define the view behavior.
class MediaView(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

    #filter_backends = [filters.SearchFilter]
    #search_fields = ['$name','$media', '$id']
    parser_classes = (JSONParser,MultiPartParser)


    @action(detail=False, methods=['put'], name='Uploader View',)
    def uploader(self, request, format=None):
        data = request.data
        serializer = MediaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data,status=201)
        return JSONResponse(serializer.errors, status=400)
        

class LandmarkPut(viewsets.ModelViewSet):
    queryset = Landmark.objects.all()
    serializer_class = LandmarkSerializer

    parser_classes = (JSONParser,MultiPartParser)

    @action(detail=False, methods=['put'], name='Landmark Put',)
    def put(self, request, format=None):
        # APPROACH 1; BUILD JSON REQUEST MANUALLY, BY EXTRACTING EACH FIELD AND THEN BUILDING DICT BY HAND
        # ACCORDING to Felix this approach actually led to the right direction, however
        # list of indeces couldn't be passed on in the request or request was sucessful, BUT wrong response was given
 
        data = request.data

        name = request.data['name']
        desc = request.data['desc']
        longitude = request.data['longitude']
        latitude = request.data['latitude']
        #get ids from request
        media_ids = request.data['media'] #<- only shows last item INSTEAD OF BEING A LIST
        text_ids = request.data['text']


        #läuft aber jetzt ist long-lat in field und das will der Felix nicht
        landmark = Landmark.objects.create(name=name,desc=desc,longitude=float(longitude),latitude=float(latitude))
        landmark.media.set(medias)
        landmark.text.set(texts)
        #hässlicher serializer
        serializer = serializers.serialize('json',[landmark,])
        '''
        print(serializer)
        try:
            return Response(serializer,status=201)
        except Exception as e:
            return Response(e, status=400)
        '''
        # APPROACH 2; classic


        put_ser = LandmarkSerializer(data=request.data)

        if put_ser.is_valid():
            put_ser.save()

            #APPROACH 3; save landmark instance with the all the indeces in the wrong format
            #then reparse the json and substitute the indeces with the actual indeces (nestes serializer)
            #throws error in the backend
            '''
            #actually get an instance of the class with the id
            medias = Media.objects.filter(id__in=media_ids)
            texts = TextBlock.objects.filter(id__in=text_ids)
        

            media_serializer = MediaSerializer(medias , many=True)
            text_serializer = TextBlockSerializer(texts , many=True)
            for medium_id in put_ser.data['media']:
                medium = Media.objects.get(pk=medium_id)
                (print(medium.name))
                for val in put_ser.data['media']:
                    print(val)
                    med_ser = MediaSerializer(medium)
                    print("medser data:", med_ser.data)
                    ind = put_ser.data['media'].index(val)
                    put_ser.data['media'][ind] = med_ser
                print("zusammengebasteltet json", put_ser.data)
            #seriliazer data {'id': 62, 'name': 'xked', 'desc': 'media 4 und 5', 'longitude': 829.6, 'latitude': 48.0, 'media': [4, 5], 'text': [4]}  
            '''
            return JsonResponse(put_ser.data, status=201)
        else:
            return JsonResponse(put_ser.errors, status=400)


class TextBlockView(viewsets.ModelViewSet):
    queryset = TextBlock.objects.all()
    serializer_class = TextBlockSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['$header','$body']

#hat keinen path||url mehr
class LandmarkView(viewsets.ModelViewSet):
    queryset = Landmark.objects.all()
    serializer_class = LandmarkSerializer
    
    #nach zahlen kann nur exzakt gefilter werden
    #mit searchfield und $ regex suche
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id']

########################################################
#for radius search
def index(request):

    return render(request, 'radius_form.html')

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

    serializer = LandmarkSerializer(queryset, many=True, context={'request': request})

    #just return the list to the radius function but render in radius
    return  queryset 

# function wo which Django view url routes is linked to!
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
#TEXTBLOCK
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
#LANDMARK
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
        #data = request.data
        media = Media.object.get(pk=1)
        text = TextBlock.object.get(pk=1)
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
        serializer = LandmarkSerializer('json',landmarks, many=True, fields=['media', 'text'])
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = request.data
        serializer = LandmarkSerializer('json',data=data, fields=['media', 'text'])
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        landmark.delete()
        return HttpResponse(status=204)

def search(request):
    if request.method == 'POST':
        search_name = request.POST.get('textfield', None)
        try:
            #landmark = Landmark.objects.filter(name = search_name) #<- exacte suche
            landmark = Landmark.objects.filter(name__contains = search_name) 
            landmark_serializer = LandmarkSerializer(landmark , many=True, context={'request': request})

            return JsonResponse(landmark_serializer.data,safe=False)
        except Landmark.DoesNotExist:
            return JsonResponse(landmark_serializer.error,404)
    else:
        return render(request, 'form.html')


##########################################################################
#MEDIA

@csrf_exempt
def media_list(request):
    """
    List all textblock entries, or create a new media entry.
    """
    if request.method == 'GET':
        medias = Media.objects.all()
        serializer = MediaSerializer(medias, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MediaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def media_detail(request, pk):
    """
    Retrieve, update or delete a media entry.
    """
    try:
        media = Media.objects.get(pk=pk)
    except Media.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MediaSerializer(media)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MediaSerializer(media, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        media.delete()
        return HttpResponse(status=204)





