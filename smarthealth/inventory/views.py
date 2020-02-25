from django.shortcuts import render
from .models import *

def itemList(request):

    item = Item.objects.all()

    context = {
        'item' : item
    }

    return render(request, 'inventory/views/inventory_items_table.html', context)

def drugList(request):

    drug = Drug.objects.all()

    context = {
        'drug' : drug
    }

    return render(request, 'inventory/views/inventory_drugs_table.html', context)