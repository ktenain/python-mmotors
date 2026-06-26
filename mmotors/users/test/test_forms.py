import datetime

from django.test import TestCase
from django.utils import timezone

from users.forms import SignupForm, ProfileForm

class SignupFormTest(TestCase):
    
    def test_email_field_label(self):
        form = SignupForm()
        self.assertTrue(form.fields['email'].label is None or form.fields['email'].label == 'Adresse mail')

    def test_first_name_field_label(self):
        form = SignupForm()
        self.assertTrue(form.fields['first_name'].label is None or form.fields['first_name'].label == 'Prénom')

    def test_last_name_field_label(self):
        form = SignupForm()
        self.assertTrue(form.fields['last_name'].label is None or form.fields['last_name'].label == 'Nom')

    def test_phone_field_label(self):
        form = SignupForm()
        self.assertTrue(form.fields['phone'].label is None or form.fields['phone'].label == 'Numéro de téléphone')

    def test_address_field_label(self):
        form = SignupForm()
        self.assertTrue(form.fields['address'].label is None or form.fields['address'].label == 'Adresse')

    def test_postcode_field_label(self):
        form = SignupForm()
        self.assertTrue(form.fields['postcode'].label is None or form.fields['postcode'].label == 'Code postal')

    def test_town_field_label(self):
        form = SignupForm()
        self.assertTrue(form.fields['town'].label is None or form.fields['town'].label == 'Ville')

class ProfileFormTest(TestCase):

    def test_email_field_label(self):
        form = ProfileForm()
        self.assertTrue(form.fields['email'].label is None or form.fields['email'].label == 'Adresse mail')

    def test_first_name_field_label(self):
        form = ProfileForm()
        self.assertTrue(form.fields['first_name'].label is None or form.fields['first_name'].label == 'Prénom')

    def test_last_name_field_label(self):
        form = ProfileForm()
        self.assertTrue(form.fields['last_name'].label is None or form.fields['last_name'].label == 'Nom')

    def test_phone_field_label(self):
        form = ProfileForm()
        self.assertTrue(form.fields['phone'].label is None or form.fields['phone'].label == 'Numéro de téléphone')

    def test_address_field_label(self):
        form = ProfileForm()
        self.assertTrue(form.fields['address'].label is None or form.fields['address'].label == 'Adresse')

    def test_postcode_field_label(self):
        form = ProfileForm()
        self.assertTrue(form.fields['postcode'].label is None or form.fields['postcode'].label == 'Code postal')

    def test_town_field_label(self):
        form = ProfileForm()
        self.assertTrue(form.fields['town'].label is None or form.fields['town'].label == 'Ville')
