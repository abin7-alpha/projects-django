from django.shortcuts import render
from django.contrib.auth.models import User
from home.views import get_categories
from productorder.models import *
from django.http import JsonResponse
import json
import datetime

"""To get the items that a user added to the cart."""
def cart(request):
    context = user_info(request)
    return render(request, 'cart.html', context)

"""To get the items in the cart to checkout those items"""
def checkout(request):
    context = user_info(request)
    return render(request, 'checkout.html', context)

"""The funtion for getting cart items,checkout items,Order we need to create/get
   is happening in here"""
def user_info(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items' : 0}

    context = {'items':items,'order': order, 'cartItems' : cartItems}

    return context

"""Json gets data from the front-end ans the funtion works in the database.
   This funtion do the purposes like adding or removing an item from the cart,
   also decrease/increase the quantity of the products according to the adding
   or removing from the cart."""
def update_item(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    action = data['action']
 
    customer = request.user.customer
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("item was added", safe=False)

"""The funtion process the final order"""
def process_order(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        #creating a shipping object for the order.
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            zipcode = data['shipping']['zipcode'],
            state = data['shipping']['state'],
        )
    else:
        print("user is not authenticated..")
    print("data :",request.body)
    return JsonResponse('payment complete', safe=False)

"""This function return's orders of a user.Only order completed objects will appear on
   the orders page."""
def user_orders(request):
    total_orders = Order.objects.filter(customer = request.user.customer)
    completed_orders = []
    
    for orders in total_orders:
        if orders.complete == True:
            completed_orders.append(orders)

    products = {}
    for order in completed_orders:
        products[order] = order.orderitem_set.all()

    context = {'productss' : products}
    return render(request, 'orders.html', context)
