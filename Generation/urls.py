from django.contrib import admin
from django.urls import path,include
from Generation import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('testing',views.testing, name='testing')
]
