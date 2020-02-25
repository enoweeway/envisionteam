from django.urls import path
from . import views


urlpatterns = [
    path('list/items/', views.itemList, name='items_list'),
    path('list/drugs/', views.drugList, name='drugs_list')
]
