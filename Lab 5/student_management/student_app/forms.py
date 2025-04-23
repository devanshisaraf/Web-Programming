from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    contact_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    english_marks = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    physics_marks = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    chemistry_marks = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
