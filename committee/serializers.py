from rest_framework import  serializers
from .models import COMMITTEE

class CommitteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = COMMITTEE
        fields = '__all__'

