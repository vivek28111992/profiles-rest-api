from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response


# Create your views here.
class HelloApiView(APIView):
  """Test API View"""

  def get(self, request, format=None):
    """Return a list of APIView features"""

    an_apiview = [
      'Uses HTTP methods as function (get, post, put, patch, delete)',
      'Is similar to traditional django view',
      'Gives you most control over you application logic',
      'Is mapped manually to URLs'
    ]

    return Response({'message': 'Hello', 'an_apiview': an_apiview})
