from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from . models import Landmark
from . serializers import LandmarkSerializer

# Create your tests here.



# tests for views

class Landmark(models.Model):
	landmark_id		= models.IntegerField(primary_key=True)
	name	= models.CharField(max_length=200)
	media    = models.CharField(max_length=200)
	n_media		= models.IntegerField()
	
	def __str__(self):     
		return self.name


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_landmark(landmark_id="", name=""):
        if landmark_id != "" and name != "":
            Landmark.objects.create(landmark_id=landmark_id, name=name)

    def setUp(self):
        # add test data
        self.create_landmark("1", "Ludwigskirch")
        self.create_landmark("2", "Langer Ludwig")
        self.create_landmark("3", "Mathildenhöhe")
        self.create_landmark("4", "Russische Kapelle")


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

