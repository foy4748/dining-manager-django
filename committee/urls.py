from django.urls import path, include

# Routers provide an easy way of automatically determining the URL conf.

# Importing Views
from committee.views import CommitteViewSet

app_name = "committee"

urlpatterns = [
    path('', CommitteViewSet.as_view({'get': 'list'}), name="all"),
]
