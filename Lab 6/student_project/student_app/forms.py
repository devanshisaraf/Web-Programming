from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    roll = forms.CharField(max_length=10, label="Roll Number")
    SUBJECTS = [
        ('Math', 'Math'),
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemistry'),
        ('Biology', 'Biology'),
        ('Computer Science', 'Computer Science'),
    ]
    subject = forms.ChoiceField(choices=SUBJECTS, label="Select Subject")
