from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import serializers
from rest_framework import status
from . import models
from . import permissions
from rest_framework import filters

# Create your views here.

class HelloApiView(APIView):
    """test api"""

    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """return APIView features"""

        an_apiview=[
            'use http methods as functions',
            'similar to a traditional django',
            'url are mapped manually '
        ]

        return Response({'message':'Hello','api_view':an_apiview})

    def post(self,request):
        """create a hello msg"""

        serializer = serializers.HelloSerializer(data= request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request, pk=None):
        """put method for updating the entity"""
        
        return Response({'method':'put'})

    def patch(self,request,pk=None):
        """Patch request, only updates fields provided in the request"""

        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        """deletes an object with key provided"""

        return Response({'method':'delete'}) 


class HellowViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """return hellow msg"""

        a_viewset=[
            'uses actions(list, create, retrive, update, partial-update)'
            'Automatically maps to urs using routers'
            'provides more functions with lets code'
        ]
        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self, request):
        """create a new hello message"""

        serializer_class= serializers.HelloSerializer(data=request.data)

        if serializer_class.is_valid():
            name= serializer_class.data.get('name')
            message='Hellow {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def retrieve(self,request,pk=None):
        """Handels getting an obj by its id"""
        return Response({'http_methods':'GET'})
    

    def update(self,request,pk=None):
        """Handles updating an obj"""

        return Response({'http_method':'PUT'})

    def partial_update(self,request, pk=None):
        """"Handles update part of an object"""

        return Response({'method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handles deleting of an object"""

        return Response({'method':'delete'})
    

class UserProfileViewSet(viewsets.ModelViewSet):
        """creating and updating profile"""

        serializer_class= serializers.UserProfileSerializer
        queryset = models.UserProfile.objects.all()
        authentication_classes = (TokenAuthentication,)
        permission_classes = (permissions.UpdateOwnProfile,)
        filter_backends = (filters.SearchFilter,)
        search_fields = ('name','email')


class LogInViewSet(viewsets.ViewSet):
    """Check email and password and return an auth token"""

    serializer_class = AuthTokenSerializer

    def create(self,request):
        """use the obtainAuthToken APIView to validate and create a token"""

        return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes= (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus,IsAuthenticated,IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""

        serializer.save(user_profile=self.request.user)
