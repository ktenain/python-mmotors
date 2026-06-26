from django.test import TestCase

from cars.models import Car, Brand, Model, Category, Gearboxe, Color, Fuel, Motorization, Option
from io import BytesIO

class BrandModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Brand.objects.create(name='Audi')

    def test_name_label(self):
        brand = Brand.objects.get(name='Audi')
        field_label = brand._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Marque')

    def test_name_max_length(self):
        brand = Brand.objects.get(name='Audi')
        max_length = brand._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

class CategotyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Citadine')

    def test_name_label(self):
        category = Category.objects.get(name='Citadine')
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Catégorie')

    def test_name_max_length(self):
        category = Category.objects.get(name='Citadine')
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

class ModelModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='Citadine')
        brand = Brand.objects.create(name='Audi')
        Model.objects.create(category=category, brand=brand, name='A1')

    def test_name_label(self):
        model = Model.objects.get(name='A1')
        field_label = model._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Modèle')

    def test_name_max_length(self):
        model = Model.objects.get(name='A1')
        max_length = model._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

class ColorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Color.objects.create(name='Rouge')

    def test_name_label(self):
        color = Color.objects.get(name='Rouge')
        field_label = color._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Couleur')

    def test_name_max_length(self):
        color = Color.objects.get(name='Rouge')
        max_length = color._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

class FuelModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Fuel.objects.create(name='Essence')

    def test_name_label(self):
        fuel = Fuel.objects.get(name='Essence')
        field_label = fuel._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Carburant')

    def test_name_max_length(self):
        fuel = Fuel.objects.get(name='Essence')
        max_length = fuel._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

class MotorizationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        fuel = Fuel.objects.create(name='Essence')
        Motorization.objects.create(fuel=fuel, name='1.2 E')

    def test_name_label(self):
        motorization = Motorization.objects.get(name='1.2 E')
        field_label = motorization._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Motorisation')

    def test_name_max_length(self):
        motorization = Motorization.objects.get(name='1.2 E')
        max_length = motorization._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

class GearboxeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Gearboxe.objects.create(name='Manuelle')

    def test_name_label(self):
        gearboxe = Gearboxe.objects.get(name='Manuelle')
        field_label = gearboxe._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Boite de vitesse')

    def test_name_max_length(self):
        gearboxe = Gearboxe.objects.get(name='Manuelle')
        max_length = gearboxe._meta.get_field('name').max_length
        self.assertEqual(max_length, 20)

class OptionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Option.objects.create(name='GPS')

    def test_name_label(self):
        option = Option.objects.get(name='GPS')
        field_label = option._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Option')

    def test_name_max_length(self):
        option = Option.objects.get(name='GPS')
        max_length = option._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

class CarModelTest(TestCase):
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

    def test_get_absolute_url(self):
        user = Car.objects.get(registration='ZZ-000-ZZ')
        self.assertEqual(user.get_absolute_url(), '/detail/1/')