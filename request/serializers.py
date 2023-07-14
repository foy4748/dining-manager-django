from rest_framework import  serializers
from .models import ACTIVATION_REQUEST, DEACTIVATION_REQUEST

class ActivationRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ACTIVATION_REQUEST
        fields = ['activation_date']

class DeactivationRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DEACTIVATION_REQUEST
        fields = ['deactivation_start_date']

