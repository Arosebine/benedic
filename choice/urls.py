from django.urls import path
from django import views
from django.urls.resolvers import URLPattern
from choice import views
from django.urls import path
from django.contrib import admin


app_name = 'choice'




urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('order_form/', views.order_form, name= 'order_form'),
    path('event/', views.event, name='event'),
    path('product/', views.product, name='product'),
]