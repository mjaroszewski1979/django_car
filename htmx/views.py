from django.shortcuts import render
from django.views import View
from . models import Car

class HomeView(View):
    
    def get(self, request):
        context = {}
        context['cars'] = Car.objects.all()

        return render(request, 'index.html', context)
