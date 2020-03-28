"""city URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#for debugging stuff

from django.conf import settings
from django.urls import re_path
from django.views.static import serve
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib.auth.models import User
import rest_framework
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers, serializers, viewsets
from webapp import views, urls


#In diesem URL DING ARBEITEN DAS SCHEINT IN DER HIERARCHIE AN DER RICHTIGEN STELLE ZU SEIN

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
# starting from the index '' (api root index)
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'media', views.MediaView)
router.register(r'landmark', views.LandmarkView)
router.register(r'textblock',views.TextBlockView)
#router.register(r'filterview',views.FilterView, basename='filter-view')






# Setting up API for automatic URL routing
# latter pattern is for enabeling browsable APIs
# just in case we need it
urlpatterns = [ 
    path('textblocks/', views.textblock_list),
    path('textblocks/<int:pk>/',views.textblock_detail),
    path('landmarks/', views.landmark_list),
    path('landmarks/<int:pk>/',views.landmark_detail),
    url(r'^index/', views.index),
    url(r'^search/', views.search),
    url(r'^radius/', views.radius),
    url(r'admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
]


# for serving media files in developing mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)