from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),  # Home page at /
    path('insert/', views.insert_data, name='insert_data'),
    path('search/', views.search_people, name='search_people'),
]
