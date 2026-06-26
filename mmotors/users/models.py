from django.contrib.auth.models import AbstractUser, Group
from django.urls import reverse
from django.db import models
from cars.models import Car

class User(AbstractUser):

    ADMINISTRATOR = 'ADMINISTRATOR'
    AFTERSALES = 'AFTERSALES'
    COMMERCIAL = 'COMMERCIAL'
    CUSTOMER = 'CUSTOMER'
    FINANCIAL = 'FINANCIAL'

    ROLE_CHOICES = (
        (ADMINISTRATOR, 'Administrateur'),
        (AFTERSALES, 'Après-ventes'),
        (COMMERCIAL, 'Commercial'),
        (CUSTOMER, 'Client'),
        (FINANCIAL, 'Financier'),
    )
    
    username = None
    email = models.EmailField(verbose_name='Adresse mail', unique=True)
    phone = models.CharField(verbose_name='Numéro de téléphone', max_length=15, blank=True, null=True)
    address = models.TextField(verbose_name='Adresse', blank=True, null=True)
    postcode = models.CharField(verbose_name='Code postal', max_length=5, blank=True, null=True)
    town = models.CharField(verbose_name='Ville', max_length=30, blank=True, null=True)
    role = models.CharField(verbose_name='Rôle', default=CUSTOMER)
    book = models.ManyToManyField(
        Car,
        limit_choices_to={'role': CUSTOMER},
        symmetrical=False,
        verbose_name='Réservation'
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.ADMINISTRATOR:
            group = Group.objects.get(name='administrators')
            group.user_set.add(self)
        elif self.role == self.AFTERSALES:
            group = Group.objects.get(name='aftersales')
            group.user_set.add(self)
        elif self.role == self.COMMERCIAL:
            group = Group.objects.get(name='commercials')
            group.user_set.add(self)
        elif self.role == self.CUSTOMER:
            group = Group.objects.get(name='customers')
            group.user_set.add(self)
        elif self.role == self.FINANCIAL:
            group = Group.objects.get(name='financials')
            group.user_set.add(self)

    def __str__(self):
        return self.email