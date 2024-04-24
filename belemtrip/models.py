from django.db import models
from django.utils.text import slugify

class Base(models.Model):
    created_at = models.DateTimeField("Criado em" , auto_now_add=True)
    updated_at = models.DateTimeField("Editado em", auto_now=True)
    active = models.BooleanField("Ativo", default=True)

    class Meta:
        abstract = True
        
class News(Base):
    title = models.CharField("Título", max_length=25)
    content = models.TextField("Conteúdo")
    website = models.URLField("Website", null=True, blank=True)
    image = models.ImageField("Imagem", upload_to="news", null=True, blank=True)
    slug = models.SlugField("Slug", max_length=50, unique=True, blank=True, editable=False )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"
class Event(Base):
    title = models.CharField("Título", max_length=25)
    description = models.TextField("Descrição")
    date = models.DateField("Data")
    location = models.CharField("Local", max_length=25 , blank=True, null=True)
    website = models.URLField("Website", null=True, blank=True)
    image = models.ImageField("Imagem", upload_to="events", null=True, blank=True)
    slug = models.SlugField("Slug", max_length=50, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

class Place(Base):
    name = models.CharField("Nome", max_length=25)
    description = models.TextField("Descrição", blank=True, null=True)
    address = models.CharField("Endereço", max_length=50)
    image = models.ImageField("Imagem", upload_to="places", null=True, blank=True)
    slug = models.SlugField("Slug", max_length=50, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Place, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locais"
        

class RestaurantCategory(Base):
    name = models.CharField("Nome", max_length=25)
    slug = models.SlugField("Slug", max_length=50, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(RestaurantCategory, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria de Restaurante"
        verbose_name_plural = "Categorias de Restaurantes"

class TouristSpotCategory(Base):
    name = models.CharField("Nome", max_length=25)
    phone = models.CharField("Telefone", max_length=15, blank=True, null=True)
    slug = models.SlugField("Slug", max_length=50, unique=True, blank=True, editable=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(TouristSpotCategory, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categoria de Ponto Turístico"
        verbose_name_plural = "Categorias de Pontos Turísticos"
        
        
class Restaurant(Place):
    STAR_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    category = models.ForeignKey(RestaurantCategory, on_delete=models.CASCADE, default=None ,verbose_name="Categoria")
    star = models.IntegerField("Estrelas", choices=STAR_CHOICES)
    website = models.URLField("Website", null=True, blank=True)
    phone = models.CharField("Telefone", max_length=15, blank=True, null=True)
    
    class Meta:
        verbose_name = "Restaurante"
        verbose_name_plural = "Restaurantes"

class Hotel(Place):
    STAR_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    star = models.IntegerField("Estrelas", choices=STAR_CHOICES)
    website = models.URLField("Website", null=True, blank=True)
    phone = models.CharField("Telefone", max_length=15, blank=True, null=True)
    
    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hoteis"

class TouristSpot(Place):
    category = models.ForeignKey(TouristSpotCategory, on_delete=models.CASCADE, default= None ,verbose_name="Categoria")
    website = models.URLField("Website", null=True, blank=True)
    phone = models.CharField("Telefone", max_length=15)
    
    class Meta:
        verbose_name = "Ponto Turístico"
        verbose_name_plural = "Pontos Turísticos"