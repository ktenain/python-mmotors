import datetime

from django.test import TestCase
from django.utils import timezone

from cars.forms import ModelSearchForm, CarSearchForm

class ModelSearchFormTest(TestCase):
    
    def test_category_field_label(self):
        form = ModelSearchForm()
        self.assertTrue(form.fields['category'].label is None or form.fields['category'].label == 'Catégorie')

    def test_brand_field_label(self):
        form = ModelSearchForm()
        self.assertTrue(form.fields['brand'].label is None or form.fields['brand'].label == 'Marque')

class CarSearchFormTest(TestCase):

    def test_model_field_label(self):
        form = CarSearchForm()
        self.assertTrue(form.fields['model'].label is None or form.fields['model'].label == 'Modèle')

    def test_gearboxe_field_label(self):
        form = CarSearchForm()
        self.assertTrue(form.fields['gearboxe'].label is None or form.fields['gearboxe'].label == 'Boite de vitesse')

    def test_color_field_label(self):
        form = CarSearchForm()
        self.assertTrue(form.fields['color'].label is None or form.fields['color'].label == 'Couleur')

    def test_price_min_field_label(self):
        form = CarSearchForm()
        self.assertTrue(form.fields['price_min'].label is None or form.fields['price_min'].label == 'Prix min')

    def test_price_max_field_label(self):
        form = CarSearchForm()
        self.assertTrue(form.fields['price_max'].label is None or form.fields['price_max'].label == 'Prix max')

    def test_price_min_low_max_field(self):
        form = CarSearchForm(data={'price_min': 1000, 'price_max': 2000})
        self.assertTrue(form.is_valid())

    def test_price_min_sup_max_field(self):
        form = CarSearchForm(data={'price_min': 2000, 'price_max': 1000})
        self.assertFalse(form.is_valid())

    def test_year_min_field_label(self):
        form = CarSearchForm()
        self.assertTrue(form.fields['year_min'].label is None or form.fields['year_min'].label == 'Année min')

    def test_year_max_field_label(self):
        form = CarSearchForm()
        self.assertTrue(form.fields['year_max'].label is None or form.fields['year_max'].label == 'Année max')

    def test_year_min_low_max_field(self):
        form = CarSearchForm(data={'year_min': 2020, 'year_max': 2025})
        self.assertTrue(form.is_valid())

    def test_year_min_sup_max_field(self):
        form = CarSearchForm(data={'year_min': 2025, 'year_max': 2020})
        self.assertFalse(form.is_valid())

    def test_mileage_min_field_label(self):
        form = CarSearchForm()
        self.assertTrue(form.fields['mileage_min'].label is None or form.fields['mileage_min'].label == 'Km min')

    def test_mileage_max_field_label(self):
        form = CarSearchForm()
        self.assertTrue(form.fields['mileage_max'].label is None or form.fields['mileage_max'].label == 'Km max')

    def test_mileage_min_low_max_field(self):
        form = CarSearchForm(data={'mileage_min': 10000, 'mileage_max': 20000})
        self.assertTrue(form.is_valid())

    def test_mileage_min_sup_max_field(self):
        form = CarSearchForm(data={'mileage_min': 20000, 'mileage_max': 10000})
        self.assertFalse(form.is_valid())

    def test_door_min_field_label(self):
        form = CarSearchForm()
        self.assertTrue(form.fields['door_min'].label is None or form.fields['door_min'].label == 'Nombre de portes min')

    def test_door_max_field_label(self):
        form = CarSearchForm()
        self.assertTrue(form.fields['door_max'].label is None or form.fields['door_max'].label == 'Nombre de portes max')

    def test_door_min_low_max_field(self):
        form = CarSearchForm(data={'door_min': 3, 'door_max': 5})
        self.assertTrue(form.is_valid())

    def test_door_min_sup_max_field(self):
        form = CarSearchForm(data={'door_min': 5, 'door_max': 3})
        self.assertFalse(form.is_valid())

    def test_place_min_field_label(self):
        form = CarSearchForm()
        self.assertTrue(form.fields['place_min'].label is None or form.fields['place_min'].label == 'Nombre de places min')

    def test_place_max_field_label(self):
        form = CarSearchForm()
        self.assertTrue(form.fields['place_max'].label is None or form.fields['place_max'].label == 'Nombre de places max')

    def test_place_min_low_max_field(self):
        form = CarSearchForm(data={'place_min': 4, 'place_max': 5})
        self.assertTrue(form.is_valid())

    def test_place_min_sup_max_field(self):
        form = CarSearchForm(data={'place_min': 5, 'place_max': 4})
        self.assertFalse(form.is_valid())

    def test_din_power_min_field_label(self):
        form = CarSearchForm()
        self.assertTrue(form.fields['din_power_min'].label is None or form.fields['din_power_min'].label == 'Puissance DIN min')

    def test_din_power_max_field_label(self):
        form = CarSearchForm()
        self.assertTrue(form.fields['din_power_max'].label is None or form.fields['din_power_max'].label == 'Puissance DIN max')

    def test_din_power_min_low_max_field(self):
        form = CarSearchForm(data={'din_power_min': 90, 'din_power_max': 110})
        self.assertTrue(form.is_valid())

    def test_din_power_min_sup_max_field(self):
        form = CarSearchForm(data={'din_power_min': 110, 'din_power_max': 90})
        self.assertFalse(form.is_valid())

    def test_tax_horsepower_min_field_label(self):
        form = CarSearchForm()
        self.assertTrue(form.fields['tax_horsepower_min'].label is None or form.fields['tax_horsepower_min'].label == 'Puissance fiscale min')

    def test_tax_horsepower_max_field_label(self):
        form = CarSearchForm()
        self.assertTrue(form.fields['tax_horsepower_max'].label is None or form.fields['tax_horsepower_max'].label == 'Puissance fiscale max')

    def test_tax_horsepower_min_low_max_field(self):
        form = CarSearchForm(data={'tax_horsepower_min': 6, 'tax_horsepower_max': 7})
        self.assertTrue(form.is_valid())

    def test_tax_horsepower_min_sup_max_field(self):
        form = CarSearchForm(data={'tax_horsepower_min': 7, 'tax_horsepower_max': 6})
        self.assertFalse(form.is_valid())