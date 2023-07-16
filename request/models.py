from django.db import models
from committee.models import COMMITTEE
from django.conf import settings

# Create your models here.

class ACTIVATION_REQUEST(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    committee_id = models.ForeignKey(COMMITTEE, on_delete=models.CASCADE, null=False)
    activation_date = models.DateField(blank=False)
    isApproved = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Activation Request'
        verbose_name_plural = 'Activation Requests'

    def __str__(self):
        return "{a} {b} {c}".format(a=self.user_id,b=self.committee_id, c=self.activation_date)

class DEACTIVATION_REQUEST(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    committee_id = models.ForeignKey(COMMITTEE, on_delete=models.CASCADE, null=False)
    isApproved = models.BooleanField(default=False)
    
    deactivation_start_date = models.DateField(blank=False)
    deactivation_end_date = models.DateField(blank=True)

    class Meta:
        verbose_name = 'Deactivation Request'
        verbose_name_plural = 'Deactivation Requests'

    def __str__(self):
        return "{a} {b} {c}".format(a=self.user_id, b=self.committee_id, c=self.deactivation_start_date)
