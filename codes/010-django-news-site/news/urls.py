
from django.urls import path

from .views import home_view, sample_api

urlpatterns = [
    path('api/', view=sample_api),
    path('', view=home_view),
]