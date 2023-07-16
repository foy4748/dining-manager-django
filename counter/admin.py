from django.contrib import admin

from .models import MEAL_COUNTER
# Register your models here.

@admin.register(MEAL_COUNTER)
class MealCounterAdmin(admin.ModelAdmin):
    list_display=("user_id", "regular_meal", "regular_meal_cost", 
                  "friday_meal", "friday_meal_cost",
                  "feast", "feast_cost"
                  )
