from django.db import models

# Create your models here.

class ACTIVATION_REQUEST(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    committee_id = models.ForeignKey('committee.COMMITTEE', on_delete=models.CASCADE, null=False)
    activation_date = models.DateField(blank=False)

    def __str__(self):
        return self.activation_date

class DEACTIVATION_REQUEST(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    committee_id = models.ForeignKey('committee.COMMITTEE', on_delete=models.CASCADE, null=False)
    
    deactivation_start_date = models.DateField(blank=False)
    deactivation_end_date = models.DateField(blank=True)
