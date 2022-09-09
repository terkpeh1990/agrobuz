from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .filters import *
# from .utils import randompassword
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import Group



def manage_profiles(request):
    profile = Profile.objects.all()

    template = 'agric/manage_profile.html'
    context ={
        'profile':profile,
        
    }
    return render(request,template,context)


def reset_staff_password(request,pk):
    profile = Profile.objects.get(id=pk)
    cc = "tempass@123"
    password = make_password(cc)
    staff = profile.user
    staff.password=password
    staff.save()
    profile.is_new = True
    profile.save()
    messages.success(request,'Password Reset Successful')
    return redirect('agric:manage_profiles')

@login_required
def populate_grouping(request):
    gr=Group.objects.all()
    for i in gr:
        Grouping_name.objects.create(name=i.name)
    messages.success(request,'User Group populated')
    return redirect('agric:manage_grouping')

def delete_grouping(request):
    gr=Grouping_name.objects.all()
    for i in gr:
        i.delete()
    messages.success(request,'User Group deleted')
    return redirect('agric:manage_grouping')

    
def manage_grouping(request):
    profile = Grouping_name.objects.all()
    template = 'agric/manage_grouping.html'
    context ={
        'profile':profile,
    }
    return render(request,template,context)

def assign_grouping(request,pk):
    profile = Profile.objects.get(id=pk)
    usergroup = Grouping_name.objects.all()
    template = 'agric/assign_grouping.html'
    context ={
        'profile':profile,
        'usergroup':usergroup,
    }
    return render(request,template,context)

def set_staff_group(request,profileid,groups):
    profile = Profile.objects.get(id=profileid)
    profile.is_staff = False
    usergroup = Grouping_name.objects.get(id=groups)
    gg = Group.objects.get(name=usergroup.name)
    profile.user.groups.clear()
    profile.user.groups.add(gg)
    if usergroup.name == 'staff':
        profile.is_staff = True
    else:
        profile.is_admin = True
   
    profile.save()
    messages.success(request,'User Group assigned  Successful')
    return redirect('agric:assign_grouping',pk=profile.id)