from rest_framework import  serializers
from .models import ACTIVATION_REQUEST, DEACTIVATION_REQUEST
from committee.models import COMMITTEE

from rest_framework.validators import UniqueForDateValidator

class ActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ACTIVATION_REQUEST
        fields = '__all__'
        # Preventing Same Date Activation Posting
        validators = [
                UniqueForDateValidator(queryset=ACTIVATION_REQUEST.objects.filter(committee_id=COMMITTEE.objects.latest('created_at')), field="user_id", date_field="activation_date")
        ]

class DeactivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DEACTIVATION_REQUEST
        fields = '__all__'
        validators = [
                UniqueForDateValidator(queryset=DEACTIVATION_REQUEST.objects.filter(committee_id=COMMITTEE.objects.latest('created_at')), field="user_id", date_field="deactivation_start_date")
        ]

