from django.shortcuts import render
from django.views.generic import ListView

from shop.models import Product, Category


def home(request):
    title = 'Теставая страница №1'
    return render(request, 'index.html', {'title': title, })


class HomeView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'category'


class CategoryProduct(ListView):
    model = Product
    template_name = ''
