from django.shortcuts import render
from django.views.generic import TemplateView
from belemtrip.models import *

class IndexView(TemplateView):
    template_name = "index.html"
    
    
