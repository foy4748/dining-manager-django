from django.urls import path, include

# Routers provide an easy way of automatically determining the URL conf.

# Importing Views
from request.views import ActivationRequestViewSet, DeactivationRequestViewSet

app_name = "request"

urlpatterns = [
    path('', ActivationRequestViewSet.as_view({'get': 'list'}), name="activationRequests"),
    path('', DeactivationRequestViewSet.as_view({'get': 'list'}), name="deactivationRequests"),
]

