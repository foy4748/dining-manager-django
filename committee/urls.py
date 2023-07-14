from django.urls import path, include
from rest_framework import routers

from .serializers import CommitteViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'committee', CommitteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
