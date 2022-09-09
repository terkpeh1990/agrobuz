from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages


def create_crop_farming(request,pk):
    bio = Bio_Data.objects.get(id=pk)
    try:
        crop_farm = Crop_Farming.objects.filter(bio=bio)
    except Crop_Farming.DoesNotExist:
        pass
    if request.method =="POST":
        form = CropFarm(request.POST)
        if form.is_valid():
            cc=form.save(commit=False)
            cc.bio = bio
            cc.save()
            CropFarming_Yeild.objects.create(crop_farming=cc,yields=cc.current_yields)
            messages.success(request, "Farm Information Added")
            return redirect("agric:create_crop_farming", pk=bio.id)
           
    else:
        form = CropFarm()
    
    template = "agric/crop_farming.html"
    context ={
        'form':form,
        'bio':bio,
        'crop_farm':crop_farm,
    }
    return render(request,template,context)


def update_crop_farming(request,pk):
    crop = Crop_Farming.objects.get(id=pk)
    bio = Bio_Data.objects.get(id=crop.bio.id)
    crop_farm= Crop_Farming.objects.filter(bio=bio)

    
    if request.method =="POST":
        form = CropFarm(request.POST,instance=crop)
        if form.is_valid():
            cc=form.save(commit=False)
            cc.bio = bio
            cc.save()
            CropFarming_Yeild.objects.create(crop_farming=cc,yields=cc.current_yields)
            messages.success(request, "Farm Information Updated")
            return redirect("agric:create_crop_farming", pk=bio.id)
           
    else:
        form = CropFarm(instance=crop)
    
    template = "agric/crop_farming.html"
    context ={
        'form':form,
        'bio':bio,
        'crop_farm':crop_farm,
    }
    return render(request,template,context)

def delete_crop_farming(request,pk):
    crop = Crop_Farming.objects.get(id=pk)
    bio = Bio_Data.objects.get(id=crop.bio.id) 
    crop.delete()
    messages.success(request,'Crop Deleted')
    return redirect("agric:create_crop_farming", pk=bio.id)

def create_profile_crop_farming(request,pk):
    bio = Bio_Data.objects.get(id=pk)
    try:
        crop_farm = Crop_Farming.objects.filter(bio=bio)
    except Crop_Farming.DoesNotExist:
        pass
    if request.method =="POST":
        form = CropFarm(request.POST)
        if form.is_valid():
            cc=form.save(commit=False)
            cc.bio = bio
            cc.save()
            CropFarming_Yeild.objects.create(crop_farming=cc,yields=cc.current_yields)
            messages.success(request, "Farm Information Added")
            return redirect("agric:view_bio", pk=bio.id)
           
    else:
        form = CropFarm()
    
    template = "agric/crop_farming.html"
    context ={
        'form':form,
        'bio':bio,
        'crop_farm':crop_farm,
    }
    return render(request,template,context)


def update_profile_crop_farming(request,pk):
    crop = Crop_Farming.objects.get(id=pk)
    bio = Bio_Data.objects.get(id=crop.bio.id)
    crop_farm= Crop_Farming.objects.filter(bio=bio)

    
    if request.method =="POST":
        form = CropFarm(request.POST,instance=crop)
        if form.is_valid():
            cc=form.save(commit=False)
            cc.bio = bio
            cc.save()
            CropFarming_Yeild.objects.create(crop_farming=cc,yields=cc.current_yields)
            messages.success(request, "Farm Information Updated")
            return redirect("agric:view_bio", pk=bio.id)
           
    else:
        form = CropFarm(instance=crop)
    
    template = "agric/crop_farming.html"
    context ={
        'form':form,
        'bio':bio,
        'crop_farm':crop_farm,
    }
    return render(request,template,context)