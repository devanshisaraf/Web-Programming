from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('insert_data')  # Redirects to /employees/insert/

urlpatterns = [
    path('', home_redirect),  # Redirect root URL to employees/insert/
    path('admin/', admin.site.urls),
    path('employees/', include('employees.urls')),
]
