from django.shortcuts import render
from datetime import date
from .forms import PromotionForm

def check_promotion(request):
    result = None
    if request.method == "POST":
        form = PromotionForm(request.POST)
        if form.is_valid():
            date_of_joining = form.cleaned_data['date_of_joining']
            experience = (date.today() - date_of_joining).days // 365
            result = "YES" if experience > 5 else "NO"
    else:
        form = PromotionForm()

    return render(request, "promotion_form.html", {"form": form, "result": result})
