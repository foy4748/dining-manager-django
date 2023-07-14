from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from committee.serializers import CommitteSerializer

from committee.models import COMMITTEE

# Create your views here.
class CommitteViewSet(viewsets.ModelViewSet):
    queryset = COMMITTEE.objects.all()
    serializer_class = CommitteSerializer
