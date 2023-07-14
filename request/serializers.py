from rest_framework import  serializers
from .models import ACTIVATION_REQUEST, DEACTIVATION_REQUEST

class ActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ACTIVATION_REQUEST
        fields = '__all__'

class DeactivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DEACTIVATION_REQUEST
        fields = '__all__'

