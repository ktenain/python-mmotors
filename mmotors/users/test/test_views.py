from django.test import TestCase
from django.urls import reverse

from users import forms
from users.models import User
#from unittest.mock import patch
from cars.models import Category, Brand, Model, Color, Fuel, Gearboxe, Option, Motorization, Car
from io import BytesIO

class signupViewTest(TestCase):
    def test_view_signup_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'users/signup.html')

""" class profileViewTest(TestCase):
    def test_view_profile_correct_template(self):
        self.client.login(username='toto@gmail.com', password='S3cret!')
        response = self.client.get(reverse('profile'))
        self.assertTemplateUsed(response, 'users/profile.html') """

""" class mybookViewTest(TestCase):
    def test_view_mybook_correct_template(self):
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

        self.client.login(username='toto@gmail.com', password='S3cret!')
        
        response = self.client.get(reverse('my-book'))
        self.assertTemplateUsed(response, 'cars/car_book.html')
 """