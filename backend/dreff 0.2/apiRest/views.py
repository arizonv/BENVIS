from django.shortcuts import render

from django.shortcuts import redirect, render
from django.http import HttpResponse
import random
from .models import Developer
from .serializers import developerSerializer
from rest_framework import generics




class developerCreate(generics.ListCreateAPIView):

    queryset =Developer.objects.all()
    serializer_class = developerSerializer

#############################################################################################################


class developerUpdata(generics.RetrieveUpdateDestroyAPIView):
    queryset =Developer.objects.all()
    serializer_class = developerSerializer


class developerDelete(generics.RetrieveDestroyAPIView):

    queryset =Developer.objects.all()
    serializer_class = developerSerializer

