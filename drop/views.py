# from django.shortcuts import render

# Create your views here.
# pages/views.py
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Drop
from .serializers import DropSerializer
from rest_framework import generics

class DropListCreate(generics.ListCreateAPIView):
    queryset = Drop.objects.all()
    serializer_class = DropSerializer


def homePageView(request):
    return HttpResponse('Hello, Please visit /admin page!')


@api_view(["GET"])
def refer(request):
    refers = ["LinkedIn", "Facebook", "Job Portals", "Another website","Through a friend","At Bkash's event"]
    return Response(status=status.HTTP_200_OK, data={"data": refers})    

# @api_view(["GET"])
# def exp_year(request):
#     years = ["Fresh Graduate", "Less than 1 year", "More than 1 year", "More than 2 years","More than 3 years","More than 4 years"]
#     return Response(status=status.HTTP_200_OK, data={"data": years})  



