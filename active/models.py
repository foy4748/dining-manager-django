from django.db import models

from django.conf import settings
from committee.models import COMMITTEE

# Create your models here.
class ACTIVE_MEAL(models.Model):
    date = models.DateField(null=False)

    # Foreign Keys
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    committee_id = models.ForeignKey(COMMITTEE, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Active Meal'
        verbose_name_plural = 'Active Meals'

    def __str__(self):
        return "{a} {b} {c}".format(a=self.user_id, b=self.committee_id, c=self.date)
