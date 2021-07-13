from django.shortcuts import render
from django.views.generic import ListView

from .models import Category


# Create your views here.

class CategoryList(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'category_data'
    paginate_by = 10
    queryset = Category.objects.all()
