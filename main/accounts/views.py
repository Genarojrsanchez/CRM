# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(req):
    # return HttpResponse("home page" || <template>) replace with render import(look at import from django)
   orders = Order.objects.all()
   customers = Customer.objects.all()

   total_customers = customers.count()

   total_orders = orders.count()
   delivered = orders.filter(status = 'Delivered').count()
   pending = orders.filter(status ='Pending').count()

   context = {'orders':orders, 'customers':customers, 'total_orders': total_orders, 'delivered': delivered, 'pending': pending}
   
   return render(req, 'accounts/dashboard.html', context)

def products(req): 
    products = Product.objects.all()
    return render(req, 'accounts/products.html', {'products': products})

def customer(req): 
    customers = Customer.object.all()
    return render(req, 'accounts/customer.html', {'customers': customers})

# def contact(req): 
#     return render(req, 'accounts/profile.html')