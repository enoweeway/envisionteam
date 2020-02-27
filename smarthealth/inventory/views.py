from django.shortcuts import render, redirect

from inventory.forms import ItemForm, DrugForm
from .models import *


def ItemPage(request):
    form = ItemForm(request.POST)
    if request.method == 'POST':
        if request.POST and form.is_valid():
            if request.user.userType == 'Client' or request.user.userType == 'Nurse':
                # obj = Item.objects.create(name=request.POST['name'],
                #                           category=request.POST['category'],
                #                           quantity=request.POST['quantity'],
                #                           date_created=request.POST['date_created'])
                form.save()
                if request.user.is_authenticated:
                    return redirect('inventory:addItem')
                else:
                    return render(request, 'authentication/views/error.html', {})
    return render(request, 'inventory/add_item.html', {'form': form})

def DrugPage(request):
    form = DrugForm(request.POST)
    if request.method == 'POST':
        if request.POST and form.is_valid():
            if request.user.userType == 'Client' or request.user.userType == 'Nurse':
                # obj = Item.objects.create(name=request.POST['name'],
                #                           category=request.POST['category'],
                #                           quantity=request.POST['quantity'],
                #                           date_created=request.POST['date_created'])
                form.save()
                if request.user.is_authenticated:
                    return redirect('inventory:addItem')
                else:
                    return render(request, 'authentication/views/error.html', {})
    return render(request, 'inventory/add_item.html', {'form': form})

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

def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.user.userType == 'Client' or request.user.userType == 'Nurse':
        item.delete()
        return redirect('inventory:items_list')
    else:
        return render(request, 'authentication/views/error.html', {})

def delete_drug(request, id):
    item = Drug.objects.get(id=id)
    if request.user.userType == 'Client' or request.user.userType == 'Nurse':
        item.delete()
        return redirect('inventory:drugs_list')
    else:
        return render(request, 'authentication/views/error.html', {})


