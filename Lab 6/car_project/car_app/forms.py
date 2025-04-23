from django import forms

class CarForm(forms.Form):
    MANUFACTURERS = [
        ('Toyota', 'Toyota'),
        ('Honda', 'Honda'),
        ('Ford', 'Ford'),
        ('BMW', 'BMW'),
        ('Tesla', 'Tesla'),
    ]
    manufacturer = forms.ChoiceField(choices=MANUFACTURERS, label="Select Manufacturer")
    model = forms.CharField(max_length=50, label="Enter Model Name")
