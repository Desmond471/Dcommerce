from django.urls import path
from . import views
from .views import homePage, aboutPage, blogPage, contactPage, shopPage, cartPage, ProductPage, BProductPage


urlpatterns = [

  path('', homePage, name='newCommerce-home'),
  path ('about/', aboutPage , name='about'),
  path ('blog/', blogPage, name='newCommerce-blog' ),
  path ('contact/', contactPage, name='newCommerce-contact'),
  path ('shop/', shopPage, name='newCommerce-shop'),
  path ('cart/', cartPage, name='newCommerce-cart'),
  path ('shop/product/', ProductPage, name='newCommerce-shop-product'),
  path ('shop/product2/', BProductPage, name='newCommerce-shop-product2'),
  path ('add_to_cart/', views.add_to_cart, name='add_to_cart'),
  path ('cart/', views.cart, name='cart'),
  path ('checkout/', views.checkout, name='checkout')
]
