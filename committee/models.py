from django.db import models

# Create your models here.
class COMMITTEE(models.Model):
    committee_no = models.IntegerField(null=False, blank=False)
    meal_rate = models.FloatField(null=False, blank=False)

    def __str__(self):
        return str(self.committee_no)
