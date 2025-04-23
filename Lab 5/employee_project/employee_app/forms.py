from django import forms
from .models import Employee

class PromotionForm(forms.Form):
    emp_id = forms.ModelChoiceField(queryset=Employee.objects.all(), label="Select Employee")
    date_of_joining = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Date of Joining")
