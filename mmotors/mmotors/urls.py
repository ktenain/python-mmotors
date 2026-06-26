"""
URL configuration for mmotors project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from django.urls import path
import users.views
import cars.views

urlpatterns = [
    path('', cars.views.home, name='home'),
    path('admin/', admin.site.urls),
    path('home/', cars.views.home, name='home'),
    path('list/<str:action>/', cars.views.car_list, name='car-list'),
    path('detail/<int:car_id>/', cars.views.car_detail, name='car-detail'),
    path('book/<int:car_id>/', cars.views.car_book, name='car-book'),
    path('unbook/<int:car_id>/', cars.views.car_unbook, name='car-unbook'),
    path('my_book/', users.views.my_book, name='my-book'),
    path('login/', LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(template_name='users/password_change_form.html'), name='password_change'),
    path('password_change-done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    path('signup/', users.views.signup, name='signup'),
    path('profile/', users.views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)