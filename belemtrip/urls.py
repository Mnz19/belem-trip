from django.urls import path
from belemtrip.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("eventos/", EventosViews.as_view(), name="eventos"),
    path("noticias/", NoticiasViews.as_view(), name="noticias"),
    path("restaurantes/", RestaurantesViews.as_view(), name="restaurantes"),
    path("hoteis/", HoteisViews.as_view(), name="hoteis"),
    path("pontos-turisticos/", PontosTuristicosViews.as_view(), name="pontos"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
