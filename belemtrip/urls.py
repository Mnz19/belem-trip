from django.urls import path
from belemtrip.views import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
