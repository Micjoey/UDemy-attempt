
from django.shortcuts import render

from math_quiz.models import Product, ShoppingCart


def index(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'math_quiz/product_list.html', context)


def show(request, id):
    context = {
        'product': Product.objects.get(id=id),
    }
    return render(request, 'math_quiz/product.html', context)
