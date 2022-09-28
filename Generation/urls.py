from django.contrib import admin
from django.urls import path,include
from Generation import views
urlpatterns = [
    path('home',views.home,name = 'home'),
    path('create',views.create,name = 'create'),
    path('steptwo',views.steptwo, name='steptwo')
]
