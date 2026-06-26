from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from cars.models import Car, Brand, Model
from django.forms import ModelForm

class ModelSearchForm(ModelForm):

   class Meta:
      model = Model
      fields = ["category", "brand"]

      def clean(self):
         super().clean()

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['category'].empty_label = ""
      self.fields["category"].required = False
      self.fields['brand'].empty_label = ""
      self.fields["brand"].required = False

class CarSearchForm(ModelForm):

   class Meta:
      model = Car
      fields = ["model", "gearboxe", "color"]

   price_min = forms.IntegerField(required=False, validators=[MinValueValidator(100), MaxValueValidator(100000)], label="Prix min")
   price_max = forms.IntegerField(required=False, validators=[MinValueValidator(100), MaxValueValidator(100000)], label="Prix max")
   year_min = forms.IntegerField(required=False, validators=[MinValueValidator(2011), MaxValueValidator(2026)], label="Année min")
   year_max = forms.IntegerField(required=False, validators=[MinValueValidator(2011), MaxValueValidator(2026)], label="Année max")
   mileage_min = forms.IntegerField(required=False, validators=[MinValueValidator(0), MaxValueValidator(300000)], label="Km min")
   mileage_max = forms.IntegerField(required=False, validators=[MinValueValidator(0), MaxValueValidator(300000)], label="Km max")
   door_min = forms.IntegerField(required=False, validators=[MinValueValidator(2), MaxValueValidator(5)], label="Nombre de portes min")
   door_max = forms.IntegerField(required=False, validators=[MinValueValidator(2), MaxValueValidator(5)], label="Nombre de portes max")
   place_min = forms.IntegerField(required=False, validators=[MinValueValidator(2), MaxValueValidator(7)], label="Nombre de places min")
   place_max = forms.IntegerField(required=False, validators=[MinValueValidator(2), MaxValueValidator(7)], label="Nombre de places max")
   din_power_min = forms.IntegerField(required=False, validators=[MinValueValidator(0), MaxValueValidator(1000)], label="Puissance DIN min")
   din_power_max = forms.IntegerField(required=False, validators=[MinValueValidator(0), MaxValueValidator(1000)], label="Puissance DIN max")
   tax_horsepower_min = forms.IntegerField(required=False, validators=[MinValueValidator(0), MaxValueValidator(100)], label="Puissance fiscale min")
   tax_horsepower_max = forms.IntegerField(required=False, validators=[MinValueValidator(0), MaxValueValidator(100)], label="Puissance fiscale max")

    # TODO ajouter des widget.attrs
    
   def clean(self):
      cleaned_data = super().clean()

      price_min = cleaned_data.get("price_min")
      price_max = cleaned_data.get("price_max")
      if price_min is not None and price_min != "" and price_max is not None and price_max != "":
         if price_max < price_min:
            raise forms.ValidationError("Le prix minimum doit être inférieur au prix maximum")
         return cleaned_data

      year_min = cleaned_data.get("year_min")
      year_max = cleaned_data.get("year_max")
      if year_min is not None and year_min != "" and year_max is not None and year_max != "":
         if year_max < year_min:
            raise forms.ValidationError("L'année minimum doit être inférieur à l'année maximum")
         return cleaned_data


      mileage_min = cleaned_data.get("mileage_min")
      mileage_max = cleaned_data.get("mileage_max")
      if mileage_min is not None and mileage_min != "" and mileage_max is not None and mileage_max != "":
         if mileage_max < mileage_min:
            raise forms.ValidationError("Le nombre de Km minimum doit être inférieur au nombre de Km maximum")
         return cleaned_data

      door_min = cleaned_data.get("door_min")
      door_max = cleaned_data.get("door_max")
      if door_min is not None and door_min != "" and door_max is not None and door_max != "":
         if door_max < door_min:
            raise forms.ValidationError("Le nombre de porte minimum doit être inférieur au nombre de porte maximum")
         return cleaned_data
      
      place_min = cleaned_data.get("place_min")
      place_max = cleaned_data.get("place_max")
      if place_min is not None and place_min != "" and place_max is not None and place_max != "":
         if place_max < place_min:
            raise forms.ValidationError("Le nombre de place minimum doit être inférieur au nombre de place maximum")
         return cleaned_data
      
      din_power_min = cleaned_data.get("din_power_min")
      din_power_max = cleaned_data.get("din_power_max")
      if din_power_min is not None and din_power_min != "" and din_power_max is not None and din_power_max != "":
         if din_power_max < din_power_min:
            raise forms.ValidationError("La puissance DIN minimum doit être inférieur à la puissance DIN maximum")
         return cleaned_data
      
      tax_horsepower_min = cleaned_data.get("tax_horsepower_min")
      tax_horsepower_max = cleaned_data.get("tax_horsepower_max")
      if tax_horsepower_min is not None and tax_horsepower_min != "" and tax_horsepower_max is not None and tax_horsepower_max != "":
         if tax_horsepower_max < tax_horsepower_min:
            raise forms.ValidationError("La puissance fiscale minimum doit être inférieur à la puissance fiscale maximum")
         return cleaned_data
      
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['model'].empty_label = ""
      self.fields["model"].disabled = True
      self.fields["model"].required = False
      self.fields['gearboxe'].empty_label = ""
      self.fields["gearboxe"].required = False
      self.fields['color'].empty_label = ""
      self.fields["color"].required = False

      # self.fields["registration"].widget.attrs.update({"class": "datePicker"})
