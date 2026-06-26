from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import render, redirect
from users import forms
from django.http import Http404
from users.models import User
from cars.models import Car
from django.contrib.auth.decorators import login_required

def signup(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'users/signup.html', context={'form': form})

def profile(request):
    form = forms.ProfileForm(instance=request.user)
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

    return render(request, 'users/profile.html', context={'form': form})

@login_required
def my_book(request):
    try:
        user = User.objects.get(email=request.user)
        car = user.book.first

        return render(request, 'cars/car_book.html', {'car': car})
    except car.DoesNotExist:
        raise Http404("Cette voiture n'existe pas")
