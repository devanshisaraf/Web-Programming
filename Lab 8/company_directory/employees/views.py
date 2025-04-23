from django.shortcuts import render, redirect
from .models import Works, Lives
from .forms import WorksForm, CompanySearchForm
from django.shortcuts import render

def home_page(request):
    return render(request, "employees/home.html")


def insert_data(request):
    if request.method == "POST":
        form = WorksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('insert_data')
    else:
        form = WorksForm()
    return render(request, "employees/insert_data.html", {"form": form})

def search_people(request):
    result = None
    if request.method == "POST":
        form = CompanySearchForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            result = Works.objects.filter(company_name=company_name).select_related()
            result = result.values('person_name', 'company_name', 'salary')
            # Fetching city data
            for person in result:
                person_obj = Lives.objects.filter(person_name=person['person_name']).first()
                if person_obj:
                    person['city'] = person_obj.city
    else:
        form = CompanySearchForm()

    return render(request, "employees/search_people.html", {"form": form, "result": result})
