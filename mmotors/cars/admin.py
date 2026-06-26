from django.contrib import admin

from cars.models import Car, Brand, Model, Color, Option, Motorization, Category, Fuel, Gearboxe

admin.site.register(Brand)

admin.site.register(Category)

admin.site.register(Color)

admin.site.register(Fuel)

admin.site.register(Gearboxe)

admin.site.register(Motorization)

admin.site.register(Option)

class ModelAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name') 

admin.site.register(Model, ModelAdmin)

# liste les champs que nous voulons sur l'affichage de la liste
class CarAdmin(admin.ModelAdmin):
    list_display = ('registration', 'model') 

admin.site.register(Car, CarAdmin)