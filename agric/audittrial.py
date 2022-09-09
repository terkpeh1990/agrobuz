from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .filters import *

@login_required
def bioaudittrail(request):

    total = Bio_Data.history.all()
    myFilter = BioFilter(request.GET, queryset=total)
    total = myFilter.qs


    template = "audittaills/bio_audit_trail.html"
    context = {
        'total': total, 'myFilter': myFilter,
    }
    return render(request, template, context)


@login_required
def businessaudittrail(request):

    total = Business_Info.history.all().order_by('-id')
    myFilter = BusinessFilter(request.GET, queryset=total)
    total = myFilter.qs

    template = "audittaills/business_audit_trail.html"
    context = {
        'total': total, 'myFilter': myFilter,
    }
    return render(request, template, context)

@login_required
def userlogs(request):

    total = AllLogin.history.all().order_by('-id')

    template = "audittaills/userlogs.html"
    context = {
        'total': total,
    }
    return render(request, template, context)

@login_required
def audittrail_view_business(request,history_id):
    bus = Business_Info.history.get(history_id=history_id)
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



    template = 'audittaills/view_trail_of_business.html'

    context = {
        'bus':bus,
        'crops':crops,
        'animal':animal,
        'association':association,
        'partners':partners,
        'bu':bu,

    }
    return render(request,template,context)


@login_required
def audittrail_view_bio(request,history_id):
    bio = Bio_Data.history.get(history_id=history_id)
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
    except Land.DoesNotExist:
        pass


    template = 'audittaills/view_trail_of_profile.html'
    context = {
        'bio':bio,
        'business':business,
        'animal':animal,
        'crops':crops,
        'association':association,

    }
    return render(request,template,context)



