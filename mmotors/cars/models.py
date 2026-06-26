from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Brand(models.Model):
    name = models.fields.CharField(max_length=100, verbose_name="Marque")

    def __str__(self):
        return f'{self.name}'

class Category(models.Model):
    name = models.fields.CharField(max_length=100, verbose_name="Catégorie")

    def __str__(self):
        return f'{self.name}'
    
class Model(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, verbose_name="Catégorie")
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL, verbose_name="Marque")
    name = models.fields.CharField(max_length=100, verbose_name="Modèle")

    def __str__(self):
        return f"{self.name}"

class Color(models.Model):
    name = models.fields.CharField(max_length=100, verbose_name="Couleur")

    def __str__(self):
        return f'{self.name}'
    
class Fuel(models.Model):
    name = models.fields.CharField(max_length=100, verbose_name="Carburant")

    def __str__(self):
        return f'{self.name}'
     
class Motorization(models.Model):
    name = models.fields.CharField(max_length=100, verbose_name="Motorisation")
    fuel = models.ForeignKey(Fuel, null=True, on_delete=models.SET_NULL, max_length=2, verbose_name="Carburant")

    def __str__(self):
        return f'{self.name}'

class Gearboxe(models.Model):
    name = models.fields.CharField(max_length=20, verbose_name="Boite de vitesse")

    def __str__(self):
        return f'{self.name}'
    
class Option(models.Model):
    name = models.fields.CharField(max_length=100, verbose_name="Option")

    def __str__(self):
        return f'{self.name}'
    
class Car(models.Model):

    created = models.fields.DateField(auto_now_add=True, verbose_name="Date de création")
    model = models.ForeignKey(Model, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Modèle")
    color = models.ForeignKey(Color, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Couleur")
    motorization = models.ForeignKey(Motorization, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Motorisation")
    registration = models.fields.CharField(unique=True, max_length=9, verbose_name="Immatriculation")
    mileage = models.fields.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(300000)], verbose_name="Kilométrage")
    year = models.fields.IntegerField(validators=[MinValueValidator(2011), MaxValueValidator(2026)], verbose_name="Année")
    door = models.fields.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(5)], verbose_name="Nombre de portes")
    place = models.fields.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(7)], verbose_name="Nombre de places")
    first_registration = models.fields.DateField(verbose_name="Mise en circulation")
    gearboxe = models.ForeignKey(Gearboxe, null=True, blank=True, on_delete=models.SET_NULL, max_length=1, verbose_name="Boite de vitesse")
    din_power = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1000)], verbose_name="Puissance DIN")
    tax_horsepower = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="Puissance fiscale")
    option = models.ManyToManyField(Option, verbose_name="Options")
    photo = models.ImageField(upload_to='cars', verbose_name="Photo")
    selling_price = models.fields.IntegerField(null=True, blank=True, validators=[MinValueValidator(5000), MaxValueValidator(100000)], verbose_name="Prix de vente")
    is_forsale = models.fields.BooleanField(default=True, verbose_name="En vente")
    rental_price = models.fields.IntegerField(null=True, blank=True, validators=[MinValueValidator(100), MaxValueValidator(1000)], verbose_name="Tarif location")
    is_forrent = models.fields.BooleanField(default=True, verbose_name="En location")
    is_available = models.fields.BooleanField(default=True, verbose_name="Disponible")

    def get_absolute_url(self):
        return reverse('car-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.registration}'