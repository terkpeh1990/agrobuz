from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from .filters import *

def create_association(request):
    if request.method =="POST":
        form = Association(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Saved Successuflly")
            return redirect("agric:manage_association")
    else:
        form = Association()
    template = "agric/create_association.html"
    context ={
        'form':form,
    }
    return render(request,template,context)

def Update_association(request,pk):
    association = Associations.objects.get(id=pk)
    if request.method =="POST":
        form = Association(request.POST,instance=association )
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successuflly")
            return redirect("agric:manage_association")   
    else:
        form = Association(instance=association)
    template = "agric/create_association.html"
    context ={
        'form':form,
    }
    return render(request,template,context)


def manage_association(request):
    
    association = Associations.objects.all()
    
    myFilter = AssociationFilter(request.GET, queryset=association)
    
    association = myFilter.qs
    
    template = 'agric/manage_associations.html'
    context = {
        'association':association,
        'myFilter':myFilter,
    }
    return render(request,template,context)


def delete_association(request,pk):
    association= Associations.objects.get(id=pk)
    association.delete()
    messages.success(request, "Association Deleted")
    return redirect("agric:manage_association")

def view_association(request,pk):
    association= Associations.objects.get(id=pk)
    try:
        association_executives = Bio_Association.objects.filter(association=association,role='Executive')
    except Bio_Association.DoesNotExist:
        pass

    try:
        association_members = Bio_Association.objects.filter(association=association,role='Member')
    except Bio_Association.DoesNotExist:
        pass
    template = 'agric/view_association.html'
    context = {
        'association':association,
        'association_executives':association_executives,
        'association_members':association_members
    }
    return render(request,template,context)

def create_bio_association(request,pk):
    bio = Bio_Data.objects.get(id=pk)
    try:
        bio_asso = Bio_Association.objects.filter(bio=bio)
    except Bio_Association.DoesNotExist:
        pass
    if request.method =="POST":
        form = BioAssociation(request.POST)
        if form.is_valid():
            cc=form.save(commit=False)
            cc.bio = bio
            cc.save()
            
            messages.success(request, "Association Information Added")
            return redirect("agric:create_bio_association", pk=bio.id)
           
    else:
        form = BioAssociation()
    
    template = "agric/bio_association.html"
    context ={
        'form':form,
        'bio':bio,
        'crop_farm':bio_asso,
    }
    return render(request,template,context)


def update_bio_association(request,pk):
    bio_asso = Bio_Association.objects.get(id=pk)
    bio = Bio_Data.objects.get(id=bio_asso.bio.id)
    association= Bio_Association.objects.filter(bio=bio)

    
    if request.method =="POST":
        form = BioAssociation(request.POST,instance=bio_asso)
        if form.is_valid():
            cc=form.save(commit=False)
            cc.bio = bio
            cc.save()
            messages.success(request, "Association Information Updated")
            return redirect("agric:create_bio_association", pk=bio.id)
           
    else:
        form = BioAssociation(instance=bio_asso)
    
    template = "agric/bio_association.html"
    context ={
        'form':form,
        'bio':bio,
        'crop_farm':association,
    }
    return render(request,template,context)

def delete_bio_association(request,pk):
    asso = Bio_Association.objects.get(id=pk)
    bio = Bio_Data.objects.get(id=asso.bio.id) 
    asso.delete()
    messages.success(request,'Association Deleted Deleted')
    return redirect("agric:create_crop_farming", pk=bio.id) 


def add_association(request,pk):
    bio = Bio_Data.objects.get(id=pk)
    if request.method =="POST":
        form = Association(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Saved Successuflly")
            return redirect("agric:create_bio_association",pk=bio.id)
    else:
        form = Association()
    template = "agric/create_association.html"
    context ={
        'form':form,
    }
    return render(request,template,context)


def create_profile_bio_association(request,pk):
    bio = Bio_Data.objects.get(id=pk)
    try:
        bio_asso = Bio_Association.objects.filter(bio=bio)
    except Bio_Association.DoesNotExist:
        pass
    if request.method =="POST":
        form = BioAssociation(request.POST)
        if form.is_valid():
            cc=form.save(commit=False)
            cc.bio = bio
            cc.save()
            
            messages.success(request, "Association Information Added")
            return redirect("agric:view_bio", pk=bio.id)
           
    else:
        form = BioAssociation()
    
    template = "agric/bio_association.html"
    context ={
        'form':form,
        'bio':bio,
        'crop_farm':bio_asso,
    }
    return render(request,template,context)


def update_profile_bio_association(request,pk):
    bio_asso = Bio_Association.objects.get(id=pk)
    bio = Bio_Data.objects.get(id=bio_asso.bio.id)
    association= Bio_Association.objects.filter(bio=bio)

    
    if request.method =="POST":
        form = BioAssociation(request.POST,instance=bio_asso)
        if form.is_valid():
            cc=form.save(commit=False)
            cc.bio = bio
            cc.save()
            messages.success(request, "Association Information Updated")
            return redirect("agric:view_bio", pk=bio.id)
           
    else:
        form = BioAssociation(instance=bio_asso)
    
    template = "agric/bio_association.html"
    context ={
        'form':form,
        'bio':bio,
        'crop_farm':association,
    }
    return render(request,template,context)