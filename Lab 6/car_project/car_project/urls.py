from django.contrib import admin
from django.urls import path
from car_app.views import car_form, display_car

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', car_form, name='car_form'),
    path('display/<str:manufacturer>/<str:model>/', display_car, name='display_car'),
]
