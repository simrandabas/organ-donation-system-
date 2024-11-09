from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
# Create your views here.
# api/views.py
from rest_framework import generics
from .models import donors, recipients
from .serializers import DonorSerializer, RecipientSerializer

# Donor views
class DonorListCreateView(generics.ListCreateAPIView):
    queryset = donors.objects.all()
    serializer_class = DonorSerializer

class DonorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = donors.objects.all()
    serializer_class = DonorSerializer

# Recipient views
class RecipientListCreateView(generics.ListCreateAPIView):
    queryset = recipients.objects.all()
    serializer_class = RecipientSerializer

class RecipientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = recipients.objects.all()
    serializer_class = RecipientSerializer
