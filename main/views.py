from django.shortcuts import render
from django.views import generic

from .models import Product


class HomeListView(generic.ListView):
    template_name = 'main/homelist.html'
    model = Product
    