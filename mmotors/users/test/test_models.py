from django.test import TestCase

from users.models import User
from django.contrib.auth.models import Group

class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Group.objects.create(name='customers')
        User.objects.create(email = 'toto@email.fr',
            phone = '0505050505',
            address = '0 rue de Paris',
            postcode = '31000',
            town = 'Toulouse',
            role='CUSTOMER')

    def test_email_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'Adresse mail')

    def test_phone_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('phone').verbose_name
        self.assertEqual(field_label, 'Numéro de téléphone')

    def test_phone_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('phone').max_length
        self.assertEqual(max_length, 15)

    def test_address_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'Adresse')

    def test_postcode_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('postcode').verbose_name
        self.assertEqual(field_label, 'Code postal')

    def test_postcode_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('postcode').max_length
        self.assertEqual(max_length, 5)

    def test_town_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('town').verbose_name
        self.assertEqual(field_label, 'Ville')

    def test_town_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('town').max_length
        self.assertEqual(max_length, 30)

    def test_role_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('role').verbose_name
        self.assertEqual(field_label, 'Rôle')
