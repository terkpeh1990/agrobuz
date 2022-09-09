from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from .filters import *

def create_bio_data(request):
    if request.method =="POST":
        form = BioForm(request.POST)
        if form.is_valid():

            cc=form.save()
            messages.success(request, "Record Saved Successuflly")

            return redirect("agric:create_business", pk=cc.id)

    else:
        form = BioForm()

    template = "agric/create_biodata.html"
    context ={
        'form':form,
    }
    return render(request,template,context)

def Update_bio_data(request,pk):
    bio = Bio_Data.objects.get(id=pk)
    if request.method =="POST":
        form = BioForm(request.POST,instance=bio)
        if form.is_valid():

            cc=form.save()
            messages.success(request, "Record Updated Successuflly")

            return redirect("agric:create_business", pk=cc.id)

    else:
        form = BioForm(instance=bio)

    template = "agric/create_biodata.html"
    context ={
        'form':form,
    }
    return render(request,template,context)

def Update_bio_profile_data(request,pk):
    bio = Bio_Data.objects.get(id=pk)
    if request.method =="POST":
        form = BioForm(request.POST,instance=bio)
        if form.is_valid():

            cc=form.save()
            messages.success(request, "Record Updated Successuflly")
            return redirect("agric:view_bio", pk=cc.id)

    else:
        form = BioForm(instance=bio)

    template = "agric/create_biodata.html"
    context ={
        'form':form,
    }
    return render(request,template,context)


def manage_biodata(request):
    bio = Bio_Data.objects.all()
    total = bio.count()
    male = bio.filter(sex__name='Male').count()
    female = bio.filter(sex__name='Female').count()

    myFilter = BioFilter(request.GET, queryset=bio)
    bio = myFilter.qs
    total = bio.count()
    male = bio.filter(sex__name='Male').count()
    female = bio.filter(sex__name='Female').count()

    template = 'agric/manage_biodata.html'

    context = {
        'bio':bio,
        'total': total,
        'male':male,
        'female':female,
        'myFilter':myFilter

    }
    return render(request,template,context)

def view_bio(request,pk):
    bio = Bio_Data.objects.get(id=pk)
    try:
        business = Business_Info.objects.filter(bio=bio.id)
    except Business_Info.DoesNotExist:
        pass
    try:
        animal = Animal_Farming.objects.filter(bio=bio.id)
    except Animal_Farming.DoesNotExist:
        pass
    try:
        crops = Crop_Farming.objects.filter(bio=bio.id)
    except Crop_Farming.DoesNotExist:
        pass

    try:
        association =Bio_Association.objects.filter(bio=bio.id)
    except Bio_Association.DoesNotExist:
        pass


    template = 'agric/view_profile.html'
    context = {
        'bio':bio,
        'business':business,
        'animal':animal,
        'crops':crops,
        'association':association,

    }
    return render(request,template,context)



def delete_biodata(request):
    bio = Bio_Data.objects.all()
    for a in bio:
        a.delete()
    return redirect('agric:manage_biodata')

def delete_bio(request,pk):
    bio = Bio_Data.objects.get(id=pk)

    bio.delete()

    messages.success(request,'Record Deleted')
    return redirect('agric:manage_biodata')