from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
# from django_rest_params.decorators import params
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import ticket
from .serializers import ticketSerializer


# Create your views here
@api_view(['POST'])
def requestRide(request):
    data = JSONParser().parse(request)
    serializer = ticketSerializer()
    if serializer.crate(data=data):
        return data['rider_id']
    else:
        return Response("No seats Avalible",status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def dropoffRide(request):
    data = JSONParser().parse(request)
    serializer = ticketSerializer()
    mes = serializer.drop(data=data)
    return Response(mes)
