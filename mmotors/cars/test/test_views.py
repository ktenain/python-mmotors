from django.test import TestCase
from django.urls import reverse
from io import BytesIO

from cars.models import Category, Brand, Model, Color, Fuel, Gearboxe, Option, Motorization, Car
from cars.forms import ModelSearchForm, CarSearchForm
from unittest.mock import patch

class HomeViewTest(TestCase):
    def test_view_list_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'car/home.html')

class CarListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        category = Category.objects.create(name='Citadine')
        brand = Brand.objects.create(name='Audi')
        model = Model.objects.create(category=category, brand=brand, name='A1')
        color = Color.objects.create(name='Rouge')
        fuel = Fuel.objects.create(name='Essence')
        motorization = Motorization.objects.create(fuel=fuel, name='1.2 E')
        gearboxe = Gearboxe.objects.create(name='Manuelle')
        option1 = Option.objects.create(name='GPS')
        option2 = Option.objects.create(name='Limiteur de vitesse')

        img = BytesIO(
            b"GIF89a\x01\x00\x01\x00\x00\x00\x00!\xf9\x04\x01\x00\x00\x00"
            b"\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01\x00\x00"
        )
        img.name = "myimage.gif"

        car = Car.objects.create(
            model=model, 
            color=color, 
            motorization=motorization, 
            registration='ZZ-000-ZZ', 
            mileage=50000, 
            year=2023, 
            door=5, 
            place=5, 
            first_registration="2023-05-15", 
            gearboxe=gearboxe,
            din_power=120,
            tax_horsepower=6,
            selling_price=15000,
            is_forsale=True,
            rental_price=250,
            is_forrent=True,
            is_available=True)
        car.option.add(option1)
        car.option.add(option2)

    def test_view_list_correct_template(self):
        response = self.client.get(reverse('car-list', args={'rent'}))
        self.assertTemplateUsed(response, 'car/car_list.html')
        
    def test_view_list_status(self):
        response = self.client.get(reverse('car-list', args={'rent'}))
        self.assertContains(response, 'Trouvez votre future voiture en location', status_code=200)

    def test_view_lists_count_cars(self):
        response = self.client.get(reverse('car-list', args={'rent'}))
        self.assertEqual(len(response.context['cars']), 1)

    def test_view_lists_count_cars_category(self):
        response = self.client.get(reverse('car-list', args={'rent'}, query={'category': 'Citadine'}))
        self.assertEqual(len(response.context['cars']), 1)

    def test_view_lists_count_cars_brand(self):
        response = self.client.get(reverse('car-list', args={'rent'}, query={'brand': 'Audi'}))
        self.assertEqual(len(response.context['cars']), 1)

    def test_view_lists_count_cars_model(self):
        response = self.client.get(reverse('car-list', args={'rent'}, query={'model': 'A1'}))
        self.assertEqual(len(response.context['cars']), 1)

    def test_view_lists_count_cars_color(self):
        response = self.client.get(reverse('car-list', args={'rent'}, query={'color': 'Rouge'}))
        self.assertEqual(len(response.context['cars']), 1)
        
    def test_view_lists_count_cars_fuel(self):
        response = self.client.get(reverse('car-list', args={'rent'}, query={'fuel': 'Essence'}))
        self.assertEqual(len(response.context['cars']), 1)
        
    def test_view_lists_count_cars_motorization(self):
        response = self.client.get(reverse('car-list', args={'rent'}, query={'motorization': '1.2 E'}))
        self.assertEqual(len(response.context['cars']), 1)
        
    def test_view_lists_count_cars_gearboxe(self):
        response = self.client.get(reverse('car-list', args={'rent'}, query={'gearboxe': 'Manuelle'}))
        self.assertEqual(len(response.context['cars']), 1)
        
    def test_view_lists_count_cars_price(self):
        response = self.client.get(reverse('car-list', args={'rent'}, query={'price_min': 100, 'price_max': 500}))
        self.assertEqual(len(response.context['cars']), 1)

    def test_view_lists_count_cars_price(self):
        response = self.client.get(reverse('car-list', args={'buy'}, query={'price_min': 10000, 'price_max': 20000}))
        self.assertEqual(len(response.context['cars']), 1)

    def test_view_lists_count_cars_year(self):
        response = self.client.get(reverse('car-list', args={'rent'}, query={'year_min': 2020, 'year_max': 2025}))
        self.assertEqual(len(response.context['cars']), 1)

    def test_view_lists_count_cars_mileage(self):
        response = self.client.get(reverse('car-list', args={'rent'}, query={'mileage_min': 40000, 'mileage_max': 60000}))
        self.assertEqual(len(response.context['cars']), 1)

    def test_view_lists_count_cars_door(self):
        response = self.client.get(reverse('car-list', args={'rent'}, query={'door_min': 4, 'door_max': 5}))
        self.assertEqual(len(response.context['cars']), 1)

    def test_view_lists_count_cars_place(self):
        response = self.client.get(reverse('car-list', args={'rent'}, query={'place_min': 4, 'place_max': 5}))
        self.assertEqual(len(response.context['cars']), 1)

    def test_view_lists_count_cars_din_power(self):
        response = self.client.get(reverse('car-list', args={'rent'}, query={'din_power_min':70, 'din_power_max': 120}))
        self.assertEqual(len(response.context['cars']), 1)

    def test_view_lists_count_cars_tax_horsepower(self):
        response = self.client.get(reverse('car-list', args={'rent'}, query={'tax_horsepower_min':5, 'tax_horsepower_max': 7}))
        self.assertEqual(len(response.context['cars']), 1)

    def test_view_detail_correct_template(self):
        car = Car.objects.get(registration='ZZ-000-ZZ')
        response = self.client.get(reverse('car-detail', args={car.id}))
        self.assertTemplateUsed(response, 'car/car_detail.html')

    def test_view_detail_status(self):
        car = Car.objects.get(registration='ZZ-000-ZZ')
        response = self.client.get(reverse('car-detail', args={car.id}))
        self.assertContains(response, 'Audi', status_code=200)

    def test_view_detail_status404(self):
        response = self.client.get(reverse('car-detail', args={9}))
        self.assertEqual(response.status_code, 404)

class CarBookViewTest(TestCase):
    def test_view_list_status(self):
        category = Category.objects.create(name='Citadine')
        brand = Brand.objects.create(name='Audi')
        model = Model.objects.create(category=category, brand=brand, name='A1')
        color = Color.objects.create(name='Rouge')
        fuel = Fuel.objects.create(name='Essence')
        motorization = Motorization.objects.create(fuel=fuel, name='1.2 E')
        gearboxe = Gearboxe.objects.create(name='Manuelle')
        option1 = Option.objects.create(name='GPS')
        option2 = Option.objects.create(name='Limiteur de vitesse')

        img = BytesIO(
            b"GIF89a\x01\x00\x01\x00\x00\x00\x00!\xf9\x04\x01\x00\x00\x00"
            b"\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01\x00\x00"
        )
        img.name = "myimage.gif"

        car = Car.objects.create(
            model=model, 
            color=color, 
            motorization=motorization, 
            registration='ZZ-000-ZZ', 
            mileage=50000, 
            year=2023, 
            door=5, 
            place=5, 
            first_registration="2023-05-15", 
            gearboxe=gearboxe,
            din_power=120,
            tax_horsepower=6,
            selling_price=15000,
            is_forsale=True,
            rental_price=250,
            is_forrent=True,
            is_available=True)
        car.option.add(option1)
        car.option.add(option2)

        response = self.client.get(reverse('car-book', args={car.id}))
        self.assertEqual(response.status_code, 302)

class CarUnbookViewTest(TestCase):
    def test_view_list_status(self):
        category = Category.objects.create(name='Citadine')
        brand = Brand.objects.create(name='Audi')
        model = Model.objects.create(category=category, brand=brand, name='A1')
        color = Color.objects.create(name='Rouge')
        fuel = Fuel.objects.create(name='Essence')
        motorization = Motorization.objects.create(fuel=fuel, name='1.2 E')
        gearboxe = Gearboxe.objects.create(name='Manuelle')
        option1 = Option.objects.create(name='GPS')
        option2 = Option.objects.create(name='Limiteur de vitesse')

        img = BytesIO(
            b"GIF89a\x01\x00\x01\x00\x00\x00\x00!\xf9\x04\x01\x00\x00\x00"
            b"\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01\x00\x00"
        )
        img.name = "myimage.gif"

        car = Car.objects.create(
            model=model, 
            color=color, 
            motorization=motorization, 
            registration='ZZ-000-ZZ', 
            mileage=50000, 
            year=2023, 
            door=5, 
            place=5, 
            first_registration="2023-05-15", 
            gearboxe=gearboxe,
            din_power=120,
            tax_horsepower=6,
            selling_price=15000,
            is_forsale=True,
            rental_price=250,
            is_forrent=True,
            is_available=True)
        car.option.add(option1)
        car.option.add(option2)

        response = self.client.get(reverse('car-unbook', args={car.id}))
        self.assertEqual(response.status_code, 302)
