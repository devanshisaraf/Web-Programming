from django.shortcuts import render, redirect
from .forms import CarForm

def car_form(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            manufacturer = form.cleaned_data['manufacturer']
            model = form.cleaned_data['model']
            return redirect('display_car', manufacturer=manufacturer, model=model)
    else:
        form = CarForm()
    return render(request, 'car_form.html', {'form': form})

def display_car(request, manufacturer, model):
    return render(request, 'display_car.html', {'manufacturer': manufacturer, 'model': model})
