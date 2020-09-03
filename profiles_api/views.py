from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status

from profiles_api import serializers


# Create your views here.
class HelloApiView(APIView):
  """Test API View"""
  serializer_class = serializers.HelloSerializers

  def get(self, request, format=None):
    """Return a list of APIView features"""

    an_apiview = [
      'Uses HTTP methods as function (get, post, put, patch, delete)',
      'Is similar to traditional django view',
      'Gives you most control over you application logic',
      'Is mapped manually to URLs'
    ]

    return Response({'message': 'Hello', 'an_apiview': an_apiview})

  def post(self, request):
    """Create a hello message with our name"""
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello {name}'
      return Response({'message': message})
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk=None):
    """Handle updating of an object"""
    return Response({'method': 'PUT'})

  def patch(self, request, pk=None):
    """Handle a partial update of an object"""
    return Response({'method': 'PATCH'})

  def delete(self, request, pk=None):
    """Delete an object"""
    return Response({'method': 'DELETE'})
