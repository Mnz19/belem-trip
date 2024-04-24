from typing import Any
from django.db.models.query import QuerySet
from django.views import View
from django.views.generic import ListView
from django.shortcuts import render
from django.views.generic import TemplateView
import requests
from belemtrip.models import *
from django.core.paginator import Paginator

class IndexView(TemplateView):
    template_name = "index.html"

class EventosViews(ListView):
    model = Event
    template_name = "eventos.html"
    context_object_name = 'eventos'
    paginate_by = 10
    
    def get_queryset(self):
        query = super().get_queryset()
        
        filtro_data = self.request.GET.get('date')
        filtro_nome = self.request.GET.get('search')
        
        if filtro_data:
            query = query.filter(date=filtro_data)
        
        if filtro_nome:
            query = query.filter(title__startswith=filtro_nome)
        
        return query
    
class NoticiasViews(TemplateView):
    template_name = "noticias.html"
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     noticias = []
    #     for x in range(1, 50):
    #         noticias.append({
    #             'title': 'Notícia ' + str(x),
    #             'description': 'Descrição da notícia ' + str(x),
    #             'image': "https://veja.abril.com.br/wp-content/uploads/2024/03/WhatsApp-Image-2024-03-25-at-10.54.15.jpeg?quality=90&strip=info&crop=1&resize=1080,565"
    #         })
    #     paginator = Paginator(noticias, 10)
    #     page_number = self.request.GET.get('page')
    #     page_obj = paginator.get_page(page_number)
        
    #     context['page_obj'] = page_obj
    #     context['noticias'] = noticias 
        
    #     return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        page = int(page)
            
        noticias = requests.get(f'https://newsapi.org/v2/everything?q=cop30&language=pt&pageSize=10&page={page}&apiKey=be2c678b0ee342eb8c9dab0f075b91eb')
        
        if noticias.status_code == 200:
            noticias = noticias.json()
            
            total_results = noticias['totalResults']
            noticias = noticias['articles']
            
            total_pages = (total_results + 10 - 1) // 10
            
            context['page_obj'] = {
                'has_previous': page > 1,
                'has_next': page < total_pages,
                'previous_page_number': max(page - 1, 1),
                'next_page_number': min(page + 1, total_pages),
                'number': page,
                'paginator': {
                    'num_pages': total_pages,
                    'page_range': range(1, total_pages + 1)
                }
            }
            context['noticias'] = noticias
        else:
            noticias = None
        return context

class RestaurantesViews(ListView):
    model = Restaurant
    template_name = "restaurantes.html"
    context_object_name = 'restaurantes'
    paginate_by = 5
    
    def get_queryset(self):
        query = super().get_queryset()
        filtro_nome = self.request.GET.get('search')
        filtro_categoria = self.request.GET.get('category')
        
        if filtro_nome:
            query = query.filter(name__startswith=filtro_nome)
        
        if filtro_categoria:
            query = query.filter(category=filtro_categoria)
        
        return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = RestaurantCategory.objects.all()
        return context
    
class HoteisViews(ListView):
    model = Hotel
    template_name = "hoteis.html"
    context_object_name = 'hoteis'
    paginate_by = 5
    
    def get_queryset(self):
        query =  super().get_queryset()
        queryset = super().get_queryset()
        filtro_nome = self.request.GET.get('search')
        filtro_star = self.request.GET.get('star')
        
        if filtro_nome:
            query = query.filter(name__startswith=filtro_nome)

        if filtro_star:
            query = query.filter(star=filtro_star)
        
        return query
    
class PontosTuristicosViews(ListView):
    model = TouristSpot
    template_name = "pontos_turisticos.html"
    context_object_name = 'pontos'
    paginate_by = 5
    
    def get_queryset(self):
        query = super().get_queryset()
        filtro_nome = self.request.GET.get('search')
        filtro_categoria = self.request.GET.get('category')
        
        if filtro_nome:
            query = query.filter(name__startswith=filtro_nome)
        
        if filtro_categoria:
            categoria_id = TouristSpotCategory.objects.filter(name=filtro_categoria).values_list('id', flat=True).first()
            if categoria_id is not None:
                query = query.filter(category=categoria_id)
        
        return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = TouristSpotCategory.objects.all()
        return context