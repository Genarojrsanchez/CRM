# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

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

def customer(req, pplInfo): 
    customer = Customer.objects.get(id=pplInfo)

    orders = customer.order_set.all()
    orderCount = orders.count()
    contexts = {'customer': customer, 'orders':orders, 'orderCount': orderCount} 
    return render(req, 'accounts/customer.html', contexts)

def createOrder(req):
    
    form = OrderForm()
    if req.method == 'POST':
        # print('Printing POST:', req.POST) #checking for output on data
        form = OrderForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(req, 'accounts/orderForm.html', context)    

def updateOrder(req, pplId):
    order = Order.objects.get(id=pplId)
    form = OrderForm(instance = order)
        # if req.method == 'POST':
    #     form = OrderForm(req.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('createOrder/')
    context = {'form':form}
    return render(req, 'accounts/orderForm.html', context)            