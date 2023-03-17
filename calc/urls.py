from django.urls import path, include

from . import views     # it means - 'from all import views'
from django.contrib import admin

urlpatterns = [
    path('',views.index, name='index'),
    path('add',views.addition, name='add'),

]