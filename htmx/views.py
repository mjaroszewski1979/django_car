from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import FormView
from django.views.generic.list import ListView
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .forms import RegisterForm
from .models import Car, UserCars
from .utils import get_max_order, reorder

class HomeView(View):
    
    def get(self, request):

        context = {}
        context['cars'] = UserCars.objects.filter(user=request.user)

        return render(request, 'index.html', context)

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Login(LoginView):
    template_name = 'login.html'

class CarList(LoginRequiredMixin, ListView):
    template_name = 'cars.html'
    model = UserCars
    context_object_name = 'cars'

    def get_template_names(self):
        if self.request.htmx:
            return 'partials/car_list_elements.html'
        return 'cars.html'
        
    def get_queryset(self):
        return UserCars.objects.prefetch_related('car').filter(user=self.request.user)

def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("This username already exists")
    else:
        return HttpResponse("This username is available")

@login_required
def add_car(request):
    car_producer = request.POST.get('car_producer')
    car = Car.objects.get_or_create(producer=car_producer)[0]
    if not UserCars.objects.filter(car=car, user=request.user).exists():
        UserCars.objects.create(car=car, user=request.user, order=get_max_order(request.user))
    cars = UserCars.objects.filter(user=request.user)
    messages.success(request, f"ADDED {car_producer.upper()} TO LIST OF CARS")
    return render(request, 'partials/car_list.html', {'cars': cars})

@login_required
@require_http_methods(['DELETE'])
def delete_car(request, id):
    UserCars.objects.get(id=id).delete()
    reorder(request.user)
    cars = UserCars.objects.filter(user=request.user)
    return render(request, 'partials/car_list.html', {'cars': cars})

@login_required
def search_car(request):
    search_text = request.POST.get('search')

    user_cars = UserCars.objects.filter(user=request.user)
    results = Car.objects.filter(producer__icontains=search_text).exclude(
        producer__in=user_cars.values_list('car__producer', flat=True)
    )
    context = {"results": results}
    return render(request, 'partials/search_results.html', context)

@login_required
def detail(request, id):
    user_car = get_object_or_404(UserCars, id=id)
    context = {"user_car": user_car}
    return render(request, 'partials/car_detail.html', context)

@login_required
def cars_partial(request):
    cars = UserCars.objects.filter(user=request.user)
    return render(request, 'partials/car_list.html', {'cars': cars})

@login_required
def upload_photo(request, id):
    user_car = get_object_or_404(UserCars, id=id)
    photo = request.FILES.get('photo')
    user_car.car.photo.save(photo.name, photo)
    context = {"user_car": user_car}
    return render(request, 'partials/car_detail.html', context)



def clear(request):
    return HttpResponse("")

def sort(request):
    cars_ids_order = request.POST.getlist('car_order')
    cars = []
    updated_cars = []
    user_cars = UserCars.objects.prefetch_related('car').filter(user=request.user)
    for index, car_id in enumerate(cars_ids_order, start=1):
        user_car = next(x for x in user_cars if x.id == int(car_id))

        if user_car.order != index:
            user_car.order = index
            updated_cars.append(user_car)
        cars.append(user_car)

        UserCars.objects.bulk_update(updated_cars, ['order'])
    return render(request, 'partials/car_list.html', {'cars': cars})
