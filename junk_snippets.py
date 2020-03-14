def(get, request)
    dlat = Radians(F('latitude') - current_lat)
    dlong = Radians(F('longitude') - current_long)

    a = (Power(Sin(dlat/2), 2) + Cos(Radians(current_lat)) 
        * Cos(Radians(F('latitude'))) * Power(Sin(dlong/2), 2)
    )

    c = 2 * ATan2(Sqrt(a), Sqrt(1-a))
    d = 6371 * c

    locationsNearMe = Landmark.objects.annotate(distance=d).order_by('distance').filter(distance__lt=10)
    serializer_class = LandmarkSerializer(locationsNearMe , many=True)

    return Response(serializer_class.data)


    
    '''
    def nearby_spots_old(request, latitude, longitude, radius=5000, limit=50):
    """
    WITHOUT use of any external library, using raw MySQL and Haversine Formula
    http://en.wikipedia.org/wiki/Haversine_formula
    """
    radius = float(radius) / 1000.0

    query = """SELECT id, (6367*acos(cos(radians(%2f))
               *cos(radians(latitude))*cos(radians(longitude)-radians(%2f))
               +sin(radians(%2f))*sin(radians(latitude))))
               AS distance FROM demo_spot HAVING
               distance < %2f ORDER BY distance LIMIT 0, %d""" % (
        float(lat),
        float(lng),
        float(lat),
        radius,
        limit
    )

    queryset = Spot.objects.raw(query)
    serializer = SpotWithDistanceSerializer(queryset, many=True)

    return JSONResponse(serializer.data)
    '''

    class FilterView(viewsets.ModelViewSet):
    queryset = Landmark.objects.all()

    serializer = LandmarkSerializer(queryset, many=True

    def get_queryset(self):
        return Landmark.objects.filter(latitude=self.kwargs.get('latitude'))

    steps get all
    filter return

    @action(methods=['get'], detail=True)
    def nearby_spots(request, latitude, longitude, radius=5000, limit=50):
        """
        WITHOUT use of any external library, using raw MySQL and Haversine Formula
        http://en.wikipedia.org/wiki/Haversine_formula
        """
        radius = float(radius) / 1000.0

        query = """SELECT id, (6367*acos(cos(radians(%2f))
                *cos(radians(latitude))*cos(radians(longitude)-radians(%2f))
                +sin(radians(%2f))*sin(radians(latitude))))
                AS distance FROM demo_spot HAVING
                distance < %2f ORDER BY distance LIMIT 0, %d""" % (
            float(latitude),
            float(longitude),
            float(latitude),
            radius,
            limit
        )

    queryset = Landmark.objects.raw(query)
    serializer = LandmarkSerializer(queryset, many=True)

    return Response(serializer.data)
import math 
from django.db.models.functions import Radians, Power, Sin, Cos, ATan2, Sqrt, Radians
from django.db.models import F
from rest_framework.decorators import action