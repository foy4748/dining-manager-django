from django.db import models

from django.conf import settings
from committee.models import COMMITTEE

# Create your models here.
class MEAL_COUNTER(models.Model):
    regular_meal = models.IntegerField(default=0,null=False)
    regular_meal_cost = models.FloatField(default=0,null=False)

    friday_meal = models.IntegerField(default=0,null=False)
    friday_meal_cost = models.FloatField(default=0,null=False)

    feast = models.IntegerField(default=0,null=False)
    feast_cost = models.FloatField(default=0,null=False)

    # Foreign Keys
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    committee_id = models.ForeignKey(COMMITTEE, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Meal Counter'
        verbose_name_plural = 'Meal Counters'

    def __str__(self):
        total_meals = self.regular_meal + self.friday_meal + self.feast
        total_cost = self.regular_meal_cost + self.friday_meal_cost + self.feast_cost
        return f'{total_cost} {total_meals}'
