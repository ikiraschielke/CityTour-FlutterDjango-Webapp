from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from . models import Landmark
from . serializers import LandmarkSerializer

# Create your tests here.



# tests for views


#debug testfile
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_landmark(landmark_id="", name="", longitude="", latitude=""):
        if landmark_id != "" and name != "" and longitude != "" and latitude != "":
            Landmark.objects.create(landmark_id=landmark_id, name=name)

    def setUp(self):
        # add test data
        self.create_landmark("1", "Ludwigskirch", "49.8681083","8.6501996")
        self.create_landmark("2", "Langer Ludwig", "49.8728581","8.6490039")
        self.create_landmark("3", "Mathildenhöhe", "49.8767891","8.6648602")
        self.create_landmark("4", "Bahnhof", "49.872571","8.6273814")


class GetAllLandmarksTest(BaseViewTest):

    def test_get_all_landmarks(self):
        """
        This test ensures that all landmarks added in the setUp method
        exist when we make a GET request to the landmarks/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("landmarks-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Landmark.objects.all()
        serialized = LandmarkSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

