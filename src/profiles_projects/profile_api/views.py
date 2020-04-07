from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status

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

    def list(self,request):
        """return hellow msg"""

        a_viewset=[
            'uses actions(list, create, retrive, update, partial-update)'
            'Automatically maps to urs using routers'
            'provides more functions with lets code'
        ]
        return Response({'message':'Hello!','a_viewset':a_viewset})