from rest_framework import routers, serializers, viewsets
from .models import COMMITTEE

class CommitteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = COMMITTEE
        fields = '__all__'

class CommitteViewSet(viewsets.ModelViewSet):
    queryset = COMMITTEE.objects.all();
    serializer_class = CommitteSerializer
