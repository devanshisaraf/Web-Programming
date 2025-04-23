from django.shortcuts import render
from student_app.forms import StudentForm


def student_form_view(request):
    form = StudentForm()
    student_data = ""
    percentage = None

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            total_marks = data['english_marks'] + data['physics_marks'] + data['chemistry_marks']
            percentage = round((total_marks / 300) * 100, 2)  # Assuming each subject is out of 100

            student_data = f"""
            Name: {data['name']}
            Date of Birth: {data['date_of_birth']}
            Address: {data['address']}
            Contact: {data['contact_number']}
            Email: {data['email']}
            Marks - English: {data['english_marks']}, Physics: {data['physics_marks']}, Chemistry: {data['chemistry_marks']}
            Total Percentage: {percentage}%
            """

    return render(request, "student_form.html", {"form": form, "student_data": student_data, "percentage": percentage})
