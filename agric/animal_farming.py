from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages

def create_animal_farming(request,pk):
    bio = Bio_Data.objects.get(id=pk)
    try:
        crop_farm = Animal_Farming.objects.filter(bio=bio)
    except Animal_Farming.DoesNotExist:
        pass
    if request.method =="POST":
        form = AnimalFarm(request.POST)
        if form.is_valid():
            cc=form.save(commit=False)
            cc.bio = bio
            cc.save()
            AnimalFarming_Yeild.objects.create(animal_farming=cc,number=cc.number)
            messages.success(request, "Farm Information Added")
            return redirect("agric:create_animal_farming", pk=bio.id)
           
    else:
        form = AnimalFarm()
    
    template = "agric/animal_farming.html"
    context ={
        'form':form,
        'bio':bio,
        'crop_farm':crop_farm,
    }
    return render(request,template,context)

def update_animal_farming(request,pk):
    crop = Animal_Farming.objects.get(id=pk)
    bio = Bio_Data.objects.get(id=crop.bio.id)
    crop_farm= Animal_Farming.objects.filter(bio=bio)

    
    if request.method =="POST":
        form = AnimalFarm(request.POST,instance=crop)
        if form.is_valid():
            cc=form.save(commit=False)
            cc.bio = bio
            cc.save()
            AnimalFarming_Yeild.objects.create(animal_farming=cc,number=cc.number)
            messages.success(request, "Farm Information Updated")
            return redirect("agric:create_animal_farming", pk=bio.id)
           
    else:
        form = AnimalFarm(instance=crop)
    
    template = "agric/animal_farming.html"
    context ={
        'form':form,
        'bio':bio,
        'crop_farm':crop_farm,
    }
    return render(request,template,context)


def delete_animal_farming(request,pk):
    crop = Animal_Farming.objects.get(id=pk)
    bio = Bio_Data.objects.get(id=crop.bio.id) 
    crop.delete()
    messages.success(request,'Animal Deleted')
    return redirect("agric:create_animal_farming", pk=bio.id)

def create_profile_animal_farming(request,pk):
    bio = Bio_Data.objects.get(id=pk)
    try:
        crop_farm = Animal_Farming.objects.filter(bio=bio)
    except Animal_Farming.DoesNotExist:
        pass
    if request.method =="POST":
        form = AnimalFarm(request.POST)
        if form.is_valid():
            cc=form.save(commit=False)
            cc.bio = bio
            cc.save()
            AnimalFarming_Yeild.objects.create(animal_farming=cc,number=cc.number)
            messages.success(request, "Farm Information Added")
            return redirect("agric:view_bio", pk=bio.id)
           
    else:
        form = AnimalFarm()
    
    template = "agric/animal_farming.html"
    context ={
        'form':form,
        'bio':bio,
        'crop_farm':crop_farm,
    }
    return render(request,template,context)

def update_profile_animal_farming(request,pk):
    crop = Animal_Farming.objects.get(id=pk)
    bio = Bio_Data.objects.get(id=crop.bio.id)
    crop_farm= Animal_Farming.objects.filter(bio=bio)

    
    if request.method =="POST":
        form = AnimalFarm(request.POST,instance=crop)
        if form.is_valid():
            cc=form.save(commit=False)
            cc.bio = bio
            cc.save()
            AnimalFarming_Yeild.objects.create(animal_farming=cc,number=cc.number)
            messages.success(request, "Farm Information Updated")
            return redirect("agric:view_bio", pk=bio.id)
           
    else:
        form = AnimalFarm(instance=crop)
    
    template = "agric/animal_farming.html"
    context ={
        'form':form,
        'bio':bio,
        'crop_farm':crop_farm,
    }
    return render(request,template,context)