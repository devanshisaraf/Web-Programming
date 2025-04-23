from django.shortcuts import render, redirect
from directory.models import Category, Page
from directory.forms import CategoryForm, PageForm

def home(request):
    categories = Category.objects.all()
    return render(request, 'directory/home.html', {'categories': categories})

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    pages = category.pages.all()
    return render(request, 'directory/category_detail.html', {'category': category, 'pages': pages})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'directory/add_category.html', {'form': form})

def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PageForm()
    return render(request, 'directory/add_page.html', {'form': form})
