from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cars.models import Car, Brand, Model, Category, Gearboxe, Color
from cars.forms import CarSearchForm, ModelSearchForm
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.http import urlencode
from django.core.mail import BadHeaderError
from users.models import User

def home(request):
    return render(request, 'car/home.html')

def car_list(request, action):

    cars_list = Car.objects.all()
    cars_list = cars_list.filter(is_available=True)
    if action == 'rent':
        cars_list = cars_list.filter(is_forrent=True)
    if action == 'buy':
        cars_list = cars_list.filter(is_forsale=True)

    #On clique sur le bouton
    if request.method == "POST":
        form = CarSearchForm(request.POST or None)
        formModel = ModelSearchForm(request.POST or None)

        if all([form.is_valid(), formModel.is_valid()]):
            try:
                base_url = reverse('car-list', args={action})

                #On nettoie les valeurs vides ou null
                cleaned = dict()
                for cle, valeur in formModel.cleaned_data.items():
                    if valeur is not None:
                        if valeur !='':
                            cleaned.update({cle: valeur})
                for cle, valeur in form.cleaned_data.items():
                    if valeur is not None:
                        if valeur !='':
                            cleaned.update({cle: valeur})

                query_string = urlencode(cleaned, False)
                url = '{}?{}'.format(base_url,query_string)
                return redirect(url)
            except BadHeaderError:
                # Si un caractère malveillant est détecté
                return HttpResponse("En-tête invalide détecté")
        
            return HttpResponseRedirect('/home/')

    else:
        form = CarSearchForm()
        formModel = ModelSearchForm()

        category_form = request.GET.get("category", "")
        brand_form = request.GET.get("brand", "")
        model_form = request.GET.get("model", "")
        gearboxe_form = request.GET.get("gearboxe", "")
        color_form = request.GET.get("color", "")

        price_min_form = request.GET.get("price_min", "")
        price_max_form = request.GET.get("price_max", "")
        year_min_form = request.GET.get("year_min", "")
        year_max_form = request.GET.get("year_max", "")
        mileage_min_form = request.GET.get("mileage_min", "")
        mileage_max_form = request.GET.get("mileage_max", "")
        door_min_form = request.GET.get("door_min", "")
        door_max_form = request.GET.get("door_max", "")
        place_min_form = request.GET.get("place_min", "")
        place_max_form = request.GET.get("place_max", "")
        din_power_min_form = request.GET.get("din_power_min", "")
        din_power_max_form = request.GET.get("din_power_max", "")
        tax_horsepower_min_form = request.GET.get("tax_horsepower_min", "")
        tax_horsepower_max_form = request.GET.get("tax_horsepower_max", "")

        if category_form is not None and category_form != "":
            cars_list = cars_list.filter(model__category__name__icontains=category_form)
        if brand_form is not None and brand_form != "":
            cars_list = cars_list.filter(model__brand__name__icontains=brand_form)
        if model_form is not None and model_form != "":
            cars_list = cars_list.filter(model__name__icontains=model_form)
        if gearboxe_form is not None and gearboxe_form != "":
            cars_list = cars_list.filter(gearboxe__name__icontains=gearboxe_form)
        if color_form is not None and color_form!= "":
            cars_list = cars_list.filter(color__name__icontains=color_form)

        if action == 'buy':
            if price_min_form is not None and price_min_form != "":
                cars_list = cars_list.filter(selling_price__gte=price_min_form)
            if price_max_form is not None and price_max_form != "":
                cars_list = cars_list.filter(selling_price__lte=price_max_form)
        if action == 'rent':
            if price_min_form is not None and price_min_form != "":
                cars_list = cars_list.filter(rental_price__gte=price_min_form)
            if price_max_form is not None and price_max_form != "":
                cars_list = cars_list.filter(rental_price__lte=price_max_form)

        if year_min_form is not None and year_min_form != "":
            cars_list = cars_list.filter(year__gte=year_min_form)
        if year_max_form is not None and year_max_form != "":
            cars_list = cars_list.filter(year__lte=year_max_form)
        if mileage_min_form is not None and mileage_min_form != "":
            cars_list = cars_list.filter(mileage__gte=mileage_min_form)
        if mileage_max_form is not None and mileage_max_form != "":
            cars_list = cars_list.filter(mileage__lte=mileage_max_form)
        if door_min_form is not None and door_min_form != "":
            cars_list = cars_list.filter(door__gte=door_min_form)
        if door_max_form is not None and door_max_form != "":
            cars_list = cars_list.filter(door__lte=door_max_form)
        if place_min_form is not None and place_min_form != "":
            cars_list = cars_list.filter(place__gte=place_min_form)
        if place_max_form is not None and place_max_form != "":
            cars_list = cars_list.filter(place__lte=place_max_form)
        if din_power_min_form is not None and din_power_min_form != "":
            cars_list = cars_list.filter(din_power__gte=din_power_min_form)
        if din_power_max_form is not None and din_power_max_form != "":
            cars_list = cars_list.filter(din_power__lte=din_power_max_form)
        if tax_horsepower_min_form is not None and tax_horsepower_min_form != "":
            cars_list = cars_list.filter(tax_horsepower__gte=tax_horsepower_min_form)
        if tax_horsepower_max_form is not None and tax_horsepower_max_form != "":
            cars_list = cars_list.filter(tax_horsepower__lte=tax_horsepower_max_form)

        cars_category = cars_list.order_by('model__category__name').values('model__category__name').distinct()
        category_list = Category.objects.all().filter(name__in=cars_category)
        formModel.fields['category'].queryset = category_list

        cars_brand = cars_list.order_by('model__brand__name').values('model__brand__name').distinct()
        brand_list = Brand.objects.all().filter(name__in=cars_brand)
        formModel.fields['brand'].queryset = brand_list

        cars_model = cars_list.order_by('model').values('model').distinct()
        model_list = Model.objects.all().filter(pk__in=cars_model)
        form.fields['model'].queryset = model_list
        form.fields["model"].disabled = False

        cars_model = cars_list.order_by('gearboxe').values('gearboxe').distinct()
        gearboxe_list = Gearboxe.objects.all().filter(pk__in=cars_model)
        form.fields['gearboxe'].queryset = gearboxe_list
        form.fields["gearboxe"].disabled = False

        cars_model = cars_list.order_by('color').values('color').distinct()
        color_list = Color.objects.all().filter(pk__in=cars_model)
        form.fields['color'].queryset = color_list
        form.fields["color"].disabled = False

        # TODO réinitialiser la valeur avec la sélection
        if category_form is not None and category_form != "":
            formModel.fields['category'].clean
            formModel.fields['category'].initial = category_form
        if brand_form is not None and brand_form != "":
            formModel.fields['brand'].initial = brand_form
        if model_form is not None and model_form != "":
            form.fields['model'].initial = model_form
        if gearboxe_form is not None and gearboxe_form != "":
            form.fields['gearboxe'].initial = gearboxe_form
        if color_form is not None and color_form!= "":
            form.fields['color'].initial = color_form

        if price_min_form is not None and price_min_form != "":
            form.fields['price_min'].initial = price_min_form
        if price_max_form is not None and price_max_form != "":
            form.fields['price_max'].initial = price_max_form
        if year_min_form is not None and year_min_form != "":
            form.fields['year_min'].initial = year_min_form
        if year_max_form is not None and year_max_form != "":
            form.fields['year_max'].initial = year_max_form
        if mileage_min_form is not None and mileage_min_form != "":
            form.fields['mileage_min'].initial = mileage_min_form
        if mileage_max_form is not None and mileage_max_form != "":
            form.fields['mileage_max'].initial = mileage_max_form
        if door_min_form is not None and door_min_form != "":
            form.fields['door_min'].initial = door_min_form
        if door_max_form is not None and door_max_form != "":
            form.fields['door_max'].initial = door_max_form
        if place_min_form is not None and place_min_form != "":
            form.fields['place_min'].initial = place_min_form
        if place_max_form is not None and place_max_form != "":
            form.fields['place_max'].initial = place_max_form
        if din_power_min_form is not None and din_power_min_form != "":
            form.fields['din_power_min'].initial = din_power_min_form
        if din_power_max_form is not None and din_power_max_form != "":
            form.fields['din_power_max'].initial = din_power_max_form
        if tax_horsepower_min_form is not None and tax_horsepower_min_form != "":
            form.fields['tax_horsepower_min'].initial = tax_horsepower_min_form
        if tax_horsepower_max_form is not None and tax_horsepower_max_form != "":
            form.fields['tax_horsepower_max'].initial = tax_horsepower_max_form

    context = {
        'action' : action,
        'cars' : cars_list,
        'form1' : formModel,
        'form2' : form,
    }
    return render(request, 'car/car_list.html',context)

def car_detail(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        raise Http404("Cette voiture n'existe pas")
   
    return render(request,
        'car/car_detail.html',
        {'car': car})

@login_required
def car_book(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        user = User.objects.get(email=request.user)
        user.book.add(car)
        car.is_available = False
        car.save()
        return render(request, 'car/car_book.html', {'car': car})
    except Car.DoesNotExist:
        raise Http404("Cette voiture n'existe pas")

@login_required
def car_unbook(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        user = User.objects.get(email=request.user)
        user.book.remove(car)
        car.is_available = True
        car.save()
        return render(request, 'car/car_detail.html', {'car': car})
    except Car.DoesNotExist:
        raise Http404("Cette voiture n'existe pas")
