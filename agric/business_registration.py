from django.shortcuts import render, redirect

from agric import association
from .models import *
from .forms import *
from django.contrib import messages
from .filters import *

def create_business(request,pk):
    bio = Bio_Data.objects.get(id=pk)
    try:
        bus= Business_Info.objects.filter(bio=bio)
    except Business_Info.DoesNotExist:
        pass

    if request.method =="POST":
        form = Business(request.POST)
        if form.is_valid():
            cc=form.save(commit=False)
            cc.bio = bio
            cc.save()
            messages.success(request, "Business Info Added")
            return redirect("agric:create_business", pk=bio.id)
    else:
        form = Business()

    template = "agric/business_registration.html"
    context ={
        'form':form,
        'bio':bio,
        'bus':bus,
    }
    return render(request,template,context)

def update_business(request,pk):
    bu = Business_Info.objects.get(id=pk)
    bio = Bio_Data.objects.get(id=bu.bio.id)
    bus = Business_Info.objects.filter(bio=bio.id)

    if request.method =="POST":
        form = Business(request.POST,instance=bu)
        if form.is_valid():
            cc=form.save(commit=False)
            cc.bio = bio
            cc.save()
            messages.success(request, "Business Info Updated")
            return redirect("agric:create_business", pk=bio.id)
    else:
        form = Business(instance=bu)

    template = "agric/business_registration.html"
    context ={
        'form':form,
        'bio':bio,
        'bus':bus,
        'bu':bu,
    }
    return render(request,template,context)




def delete_business(request,pk):
    bus= Business_Info.objects.get(id=pk)
    ff = bus.bio.id
    bus.delete()
    messages.success(request, "Business Deleted")
    return redirect("agric:create_business",pk=ff)


def create_partner(request,pk):
    bus = Business_Info.objects.get(id=pk)
    bu = Business_Partners.objects.filter(business=bus.id)
    data = Bio_Data.objects.all()


    template = "agric/partner.html"
    context ={

        'bus':bus,
        'bu':bu,
        'data':data,
    }
    return render(request,template,context)




def add_partner(request,pk,bus):

    bus = Business_Info.objects.get(id=bus)
    data = Bio_Data.objects.get(id=pk)
    bio = Business_Partners.objects.create(bio=data,business=bus)
    messages.success(request,'Business Partner Added')
    return redirect('agric:create_partner',pk=bus.id)


def delete_partner(request,pk):
    bus= Business_Partners.objects.get(id=pk)
    ff = bus.business.id
    bus.delete()
    messages.success(request, "Partner Removed")
    return redirect("agric:create_partner",pk=ff)


def manage_business(request):
    bus = Business_Info.objects.all()
    total = bus.count()
    male = bus.filter(bio__sex__name ='Male').count()
    female = bus.filter(bio__sex__name ='Female').count()
    unregistered = bus.filter(registration_status='No').count()

    myFilter = BusinessFilter(request.GET, queryset=bus)
    bus = myFilter.qs
    total = bus.count()
    male = bus.filter(bio__sex__name ='Male').count()
    female = bus.filter(bio__sex__name ='Female').count()
    unregistered = bus.filter(registration_status='No').count()

    template = 'agric/manage_business.html'

    context = {
        'bus':bus,
        'total': total,
        'male':male,
        'female':female,
        'unregistered':unregistered,
        'myFilter':myFilter,

    }
    return render(request,template,context)

def agri_business_d(request):
    object_status_list2 = [
        "Farmers","Tractor Operators","Input Dealers","Marketers/Aggregators",
        "Processors","Transporters","Consumers","Traders"
        ]
    bus = Business_Info.objects.filter(value_chain__name__in=object_status_list2)
    total = bus.count()
    male = bus.filter(bio__sex__name ='Male').count()
    female = bus.filter(bio__sex__name ='Female').count()
    unregistered = bus.filter(registration_status='No').count()

    myFilter = BusinessFilter(request.GET, queryset=bus)
    bus = myFilter.qs
    total = bus.count()
    male = bus.filter(bio__sex__name ='Male').count()
    female = bus.filter(bio__sex__name ='Female').count()
    unregistered = bus.filter(registration_status='No').count()

    template = 'agric/manage_business.html'

    context = {
        'bus':bus,
        'total': total,
        'male':male,
        'female':female,
        'unregistered':unregistered,
        'myFilter':myFilter,

    }
    return render(request,template,context)


def view_business(request,pk):
    bus = Business_Info.objects.get(id=pk)
    try:
        bu =Business_ic.objects.filter(business=bus.id)
    except Business_ic.DoesNotExist:
        pass
    partners = Business_Partners.objects.filter(business=bus.id)
    crops = Crop_Farming.objects.filter(bio=bus.bio.id)
    animal = Animal_Farming.objects.filter(bio=bus.bio.id)

    object_association_list = []
    object_association_list.append(bus.bio.id)
    for i in partners:
        object_association_list.append(i.bio.id)
    for b in object_association_list:
        print(b)
    association = Bio_Association.objects.filter(bio = object_association_list)



    template = 'agric/view_business.html'

    context = {
        'bus':bus,
        'crops':crops,
        'animal':animal,
        'association':association,
        'partners':partners,
        'bu':bu,

    }
    return render(request,template,context)


def create_profile_business(request,pk):
    bio = Bio_Data.objects.get(id=pk)
    try:
        bus= Business_Info.objects.filter(bio=bio)
    except Business_Info.DoesNotExist:
        pass

    if request.method =="POST":
        form = Business(request.POST)
        if form.is_valid():
            cc=form.save(commit=False)
            cc.bio = bio
            cc.save()
            messages.success(request, "Business Info Added")
            return redirect("agric:view_bio", pk=bio.id)
    else:
        form = Business()

    template = "agric/business_registration.html"
    context ={
        'form':form,
        'bio':bio,
        'bus':bus,
    }
    return render(request,template,context)

def update_profile_business(request,pk):
    bu = Business_Info.objects.get(id=pk)
    bio = Bio_Data.objects.get(id=bu.bio.id)
    bus = Business_Info.objects.filter(bio=bio.id)

    if request.method =="POST":
        form = Business(request.POST,instance=bu)
        if form.is_valid():
            cc=form.save(commit=False)
            cc.bio = bio
            cc.save()
            messages.success(request, "Business Info Updated")
            return redirect("agric:view_bio", pk=bio.id)
    else:
        form = Business(instance=bu)

    template = "agric/business_registration.html"
    context ={
        'form':form,
        'bio':bio,
        'bus':bus,
        'bu':bu,
    }
    return render(request,template,context)


def add_ic_code(request,pk):
    bu = Business_Info.objects.get(id=pk)
    bio = Bio_Data.objects.get(id=bu.bio.id)
    bus = Business_Info.objects.filter(bio=bio.id)
    c = Ica_code.objects.all()
    try:
        vv = Business_ic.objects.filter(business=bu.id)
    except Business_ic.DoesNotExist:
        pass

    if request.method =="POST":
        form = Business(request.POST,instance=bu)
        loca = request.POST.get("code")

        print(loca)
        try:
            loc = Ica_code.objects.get(sub_description=loca)
        except Ica_code.DoesNotExist:
            messages.success(request,"Code Not Avialable")
            return redirect('agric:add_ic_code')

        Business_ic.objects.create(business = bu,code= loc)

        messages.success(request, "Business Code Added")
        return redirect("agric:add_ic_code", pk=bu.id)
    else:
        form = Business(instance=bu)

    template = "agric/ic_code.html"
    context ={
        'form':form,
        'bio':bio,
        'bus':bus,
        'bu':bu,
        'c':c,
        'vv':vv
    }
    return render(request,template,context)

def delete_code(request,pk):
    bus= Business_ic.objects.get(id=pk)
    ff = bus.business.id
    bus.delete()
    messages.success(request, "Code Removed")
    return redirect("agric:add_ic_code",pk=ff)