from django.contrib import admin
from django.urls import path
from employee_app.views import check_promotion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', check_promotion, name='check_promotion'),
]
