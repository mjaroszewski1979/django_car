from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegisterForm
from .models import UserCars


class HomeView(View):

    """HomeView Class which is responsile for rendering index page"""
    
    def get(self, request):
        """
        This is a method responsible for handling HTTP GET requests
        :param request: HttpRequest object
        """
        return render(request, 'index.html')

class SphinxView(View):
    
    def get(self, request):
        return render(request, 'sphinx.html')

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


