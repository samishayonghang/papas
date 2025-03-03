from django.urls import path
from.views import personal

urlpatterns = [
    path('', personal , name="personal"),
]
