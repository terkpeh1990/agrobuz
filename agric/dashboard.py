from django.shortcuts import render, redirect
from agric import association
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Sum ,Q,Count
from django.http import JsonResponse
import json

def home(request):
    object_status_list = ["Peasant Farmer", "Commercial Farmer",]
    object_status_list2 = [
        "Farmers","Tractor Operators","Input Dealers","Marketers/Aggregators",
        "Processors","Transporters","Consumers","Traders"
        ]
    bus = Value_Chain.objects.all()
    sdata =bus.values('name').annotate(c =Count('business_info__id'),).values('name','c').exclude(c__lte=0).order_by('c')
    agric = Value_Chain.objects.filter(name__in =object_status_list2)
    data2 =agric.values('name').annotate(c =Count('business_info__id'),).values('name','c').exclude(c__lte=0).order_by('c')
    
    loca =  Location.objects.all()
    location_stats = loca.values('name').annotate(c =Count('bio_data__business_info__id'),).values('name','c').exclude(c__lte=0).order_by('c')
    tot = Bio_Data.objects.all()
    total = tot.count()
    total_male = tot.filter(sex__name='Male').count()
    total_female = tot.filter(sex__name='Female').count()
    unregistered = Business_Info.objects.filter(registration_status='No').count()
    agri_business = Business_Info.objects.filter(value_chain__name__in=object_status_list2)
    nonagri_business = Business_Info.objects.exclude(value_chain__name__in=object_status_list2).count()
    total_agric = agri_business.count()
    total_male_agric =agri_business.filter(bio__sex__name='Male').count()
    total_female_agric =agri_business.filter(bio__sex__name='Female').count()
    male_led = agri_business.filter(led_by_woman='No').count()
    female_led = agri_business.filter(led_by_woman='Yes').count()

    labels = []
    data = []
    dd = Sex.objects.all()
    sex_stass =dd.values('name').annotate(c =Count('bio_data__business_info__id')).values('name','c').order_by('c')
    for sex in sex_stass:
        labels.append(sex['name'])
        data.append(sex['c'])
    label = []
    datas = []
    data3 =agric.values('name').annotate(v =Count('bio_data__business_info__id'),).values('name','v').exclude(v__lte=0).order_by('v')
    for chain in data3:
        label.append(chain['name'])
        datas.append(chain['v'])

    categories = list()
    agr_data = list()
    for entry in data3:
        categories.append('%s' % entry['name'])
        agr_data.append(entry['v'])

    

    template='agric/dashboard.html'
    context ={
        'sdata':sdata,
        'data2':data2,
        'total':total,
        'location_stats':location_stats,
        'total_male':total_male,
        'total_female':total_female,
        'unregistered':unregistered,
        'total_agric':total_agric,
        'total_male_agric':total_male_agric,
        'total_female_agric':total_female_agric,
        'nonagri_business':nonagri_business,
        'labels': labels,
        'data': data,
        'label': label,
        'datas': datas,
        'male_led':male_led,
        'female_led':female_led,
       
        
    }
    return render(request,template,context)


