from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from os import *
from Vendor.models import *
from .models import *
from Email.views import Email

# Create your views here.
def indexPage(request):
    if request.session.get('is_authenticated', False):
        cust_unique_keyid = request.session['cust_unique_keyid']
        user_id = Customers.objects.get(cust_unique_keyid = cust_unique_keyid)
        Cart.objects.filter(cust_id = user_id).count()
        context = {
            'games' : Games.objects.all(),
            'cart_count' : Cart.objects.filter(cust_id = user_id).count()
        }
        return render(request, 'index.html',context)
    else:
        context = {
            'games' : Games.objects.all()
        }
        return render(request, 'index.html', context)

def render_account_page(request):
    if request.session.get('is_authenticated', False):
        user_data = Customers.objects.get(cust_unique_keyid = request.session['cust_unique_keyid'])
        return render(request, 'user_account.html', context={'user_data': user_data})
    else:
        return redirect(reverse('render_customer_login_page'))

def view_cart(request):
    if request.session.get('is_authenticated', False):
        # user = request.session['cust_email']
        # user_id = Customers.objects.get(cust_email = user)
        # cart = Cart.objects.filter(cust_id=user_id.cust_id)
        # return HttpResponse(cart[0].cart_id)
         
        # cartitem = CartItems.objects.get(cart_id=cart.cart_id)

        #game = Games.objects.filter(gid = cartitem.game.gid)

        # return render(request, 'Cart/viewcart.html',context = {'game':game,})
        return render(request, 'Cart/cart.html')
    else:
        return redirect(reverse('render_customer_login_page'))

def add_to_cart(request,id):
    
    if request.session.get('is_authenticated', False):
        game = Games.objects.get(product_key = id)
        user = request.session['cust_unique_keyid']
        user_id = Customers.objects.get(cust_unique_keyid = user)
        #return HttpResponse(user_id.cust_id)
        try:
            cart = Cart.objects.create(
                cust_id = user_id,
                is_paid = False
            )
            cartitem = CartItems.objects.create(cart = cart, game = game)
            
        except Exception as e:
            return HttpResponse(e)
        return redirect(reverse(indexPage))
    else:
        return redirect(reverse('render_customer_login_page'))
        