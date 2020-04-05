from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """test api"""

    def get(self, request, format=None):
        """return APIView features"""

        an_apiview=[
            'use http methods as functions',
            'similar to a traditional django',
            'url are mapped manually '
        ]

        return Response({'message':'Hello','api_view':an_apiview})

