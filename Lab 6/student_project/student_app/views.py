from django.shortcuts import render, redirect
from .forms import StudentForm

def first_page(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            request.session['name'] = form.cleaned_data['name']
            request.session['roll'] = form.cleaned_data['roll']
            request.session['subject'] = form.cleaned_data['subject']
            return redirect('second_page')
    else:
        form = StudentForm()

    return render(request, 'firstPage.html', {'form': form})

def second_page(request):
    name = request.session.get('name', 'Unknown')
    roll = request.session.get('roll', 'Unknown')
    subject = request.session.get('subject', 'Unknown')
    return render(request, 'secondPage.html', {'name': name, 'roll': roll, 'subject': subject})
