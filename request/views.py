from django.shortcuts import render
# Create your views here.

from rest_framework import viewsets
from rest_framework import permissions
from request.serializers import ActivationRequestSerializer, DeactivationRequestSerializer

from request.models import ACTIVATION_REQUEST, DEACTIVATION_REQUEST

# Create your views here.
class ActivationRequestViewSet(viewsets.ModelViewSet):
    queryset = ACTIVATION_REQUEST.objects.all()
    serializer_class = ActivationRequestSerializer

class DeactivationRequestViewSet(viewsets.ModelViewSet):
    queryset = DEACTIVATION_REQUEST.objects.all()
    serializer_class = DeactivationRequestSerializer
