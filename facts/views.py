from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def facts_list(request):
    return Response([
        {"id": 1, "fact": "The sun is a star."},
        {"id": 2, "fact": "Water boils at 100°C."},
        {"id": 3, "fact": "Earth has one moon."}
    ])
