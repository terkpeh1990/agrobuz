from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages

def create_land_info(request,pk):
    bus = Business_Info.objects.get(id=pk)
    
    try:
        bu = Land.objects.filter(business=bus.id)
    except Land.DoesNotExist:
        pass
    
    if request.method =="POST":
        form = Lands(request.POST)
        if form.is_valid():
            cc=form.save(commit=False)
            cc.business = bus
            cc.bio = bus.bio
            cc.save()
            messages.success(request, "Land Info Added")
            return redirect("agric:create_land_info", pk=bus.id)
    else:
        form = Lands()
    
    template = "agric/land_info.html"
    context ={
        'form':form,
         
        'bus':bus,
        'bu':bu,
    }
    return render(request,template,context)



