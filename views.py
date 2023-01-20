from django.shortcuts import HttpResponse, render
from product.models import Product
import datetime

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')

def product_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        context = {
            'product': product
        }
        return render(request, 'product/product.html', context=context)
def project(request):
    if request.method == 'GET':
        return HttpResponse('Hi! its my first project')

def good_bye(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!')
def date(request):
    if request.method == 'GET':
        return HttpResponse(datetime.datetime.now().date)

