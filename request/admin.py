from django.contrib import admin

from request.models import ACTIVATION_REQUEST, DEACTIVATION_REQUEST

# Register your models here.
admin.site.register(ACTIVATION_REQUEST)
admin.site.register(DEACTIVATION_REQUEST)
