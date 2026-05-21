from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Product, Cart, CartItem
from django.contrib.auth.decorators import login_required


def homePage(request):
    context={
        'context: context'
    }
    return render(request, 'index.html')

def aboutPage(request):
    context={
        'context: context'
    }
    return render(request, 'about.html',)

def blogPage(request):
    context={
        'context: context'
    }
    return render(request, 'blog.html',)

def contactPage(request):
    context={
        'context: context'
    }
    return render(request, 'contact.html',)

def shopPage(request):
     products = Product.objects.all()

     return render(request, 'shop.html',{'products':products})


def cartPage(request):
    carts = CartItem.objects.all()
    return render(request, 'cart.html',{'cart_items': carts})

def ProductPage(request):
    context={
        'context: context'
    }
    return render(request, 'product.html',{})

def BProductPage(request):
    context={
        'context: context'
    }
    return render(request, 'product2.html',)

# def product_page( request ):
#     products = Product.objects.all()
#     return render(request, 'product_page.html',{'products':products})
    
def add_to_cart(request, product_id):
    product= Product.objects.get(id= product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if created:
        cart_item.quantity += 1
        cart_item.save()
    return 
JsonResponse({'message' :'Product added to cart successfully'})

def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request,'cart.html',{'cart_items' : cart_items
         })

def checkout(request):
    #implement checkout logic here 
    pass





# Create your views here.
