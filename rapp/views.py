from argparse import Action
from http.client import CREATED
from itertools import product
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from multiprocessing import context
from rlcompleter import Completer
from turtle import update
from venv import create
from rapp.models import *
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.http import JsonResponse

# from django.contrib.admin import auth


# Create your views here.

def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitems_set.all()
        cartitems = order.cartitemtotal     
    else:
        items=[]
        order={'carttotal': 0 , 'cartitemtotal':0 , 'shipping':False} 
        cartitems = order['cartitemtotal']
        
    products = Product.objects.all()
    context = {'products':products , 'cartitems':cartitems} 
    return render (request,"store.html",context)
   


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitems_set.all()
        cartitems = order.cartitemtotal  
        # print(items)
        # print(customer)
        # print(order)
    else:
        items=[]
        order={'carttotal': 0 , 'cartitemtotal':0 , 'shipping':False}
        cartitems = order['cartitemtotal']

    context ={'items':items , 'order':order , 'cartitems':cartitems}
    
    return render (request,"cart.html",context)   


        
     

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer, complete = False )
        items = order.orderitems_set.all()
        cartitems = order.cartitemtotal 
        # print(items)
        # print(customer)
        # print(order)
    else:
        items=[]
        order={'carttotal': 0 , 'cartitemtotal':0 , 'shipping':False}
        cartitems = order['cartitemtotal']    

    context ={'items':items , 'order':order , 'cartitems':cartitems}
    
    return render (request,"checkout.html",context)
      
@csrf_exempt
def updateitem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('action:' , action)
    print('productId:' , productId)

   

    customer =  request.user.customer
    product = Product.objects.get( id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItems.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity =(orderItem.quantity -1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('item was add', safe=False)

@csrf_exempt
def processorder(request):
    transaction_id = datetime.datetime.now().timestamp()
    print(transaction_id)
    data = json.loads(request.body)
    print(data)
    print('data:', request.body)    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        if total == order.cartitemtotal:
            order.complete = True
        order.save()

        if order.shipping == False:
            Shippingaddress.objects.create(
            customer=customer,
            order=order,
            Address=data['shipping']['address'],
            state=data['shipping' ]['state'],
            zip_code=data['shipping'] ['zip'],
            )
    else:
        print('User is not logged in ..')
    return JsonResponse(' Payment complete! ' , safe=False)


    

def payment(request):
    return HttpResponse('payment')    
