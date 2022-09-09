from django import forms
from django.db.models import fields
from .import models
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Location,Sex,Marital_Status,Value_Chain,Associations


User = get_user_model()

class DateInput(forms.DateInput):
    input_type = 'date'




class BioForm(forms.ModelForm):
    
    value_chain=forms.ModelChoiceField(
        queryset=Value_Chain.objects.exclude(name='Farmers').order_by('name'))
    
    class Meta:
        model = models.Bio_Data
        exclude =('id',)

        widgets = {
            'dob': DateInput(),
        }

        labels = {
                
                'dob': 'Date of Birth',
                'valid_id': 'Valid ID (Ghana Card)',

                
            }

class CropFarm(forms.ModelForm):
    
    class Meta:
        model = models.Crop_Farming
        exclude =('bio',)

       
        labels = {
                
                'crop': 'Select Crop',
                'size': 'Farm Size(In Acres)',
                'current_yields':'Current Yield(Bags)',
            }


class AnimalFarm(forms.ModelForm):
    
    class Meta:
        model = models.Animal_Farming
        exclude =('bio',)

       
        labels = {
                
                'animal': 'Select Animal',
                'number':'Current Number',
            }


class Association(forms.ModelForm):
    object_status_list = ["Peasant Farmer", "Commercial Farmer"]
    value_chain=forms.ModelChoiceField(
        queryset=Value_Chain.objects.exclude(name__in=object_status_list).order_by('name'))
    
    class Meta:
        model = models.Associations
        fields='__all__'

       
        labels = {
                'name':'Name Of Associations/FBO/LBO',
                'male_members': 'Total Male Members',
                'female_members':'Total Female Members',
            }

class BioAssociation(forms.ModelForm):
    association=forms.ModelChoiceField(
        queryset=Associations.objects.all().order_by('name'),label=False)

    
    
    class Meta:
        model = models.Bio_Association
        exclude =('bio',)

       
        labels = {
                
                'association': 'Association/FBO/LBO',
                'role':'Role',
            }

class Business(forms.ModelForm):

    object_status_list = ["Peasant Farmer", "Commercial Farmer"]
    value_chain=forms.ModelChoiceField(
        queryset=Value_Chain.objects.exclude(name__in=object_status_list).order_by('name'))
    
    class Meta:
        model = models.Business_Info
        exclude =('id',)

       
        labels = {
                'name': 'Name of Farm/Business',
                'permit':'Permit No.',
                'tin_number':'Tin Number',
                'permanent_staff_no': 'No. Of Permanent Staff',
                'casual_staff_no': 'No. Of Casual Staff',
                'registration_status': 'Registrated With Assembly?',
                'type_ownership':'Type of Ownership',
                'scale':'Business Scale',
                'owned_by_woman':'Woman Owned ?',
                'led_by_woman':'Woman Led ?',
                'total_land_area_of_farm':'Total Land Area of Farm(In Acres)',
                'total_area_under_cultivation':'Total Area Under Cultivation(In Acres)',
                'land_title_status':'land Status',
            }


# class Lands(forms.ModelForm):
    
    
    
#     class Meta:
#         model = models.Land
#         exclude =('business',)


class CreateUserForm(UserCreationForm):
    

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        user_exists = User.objects.filter(username=username)
       
        if email:
            if user_exists.exists():
                raise forms.ValidationError(
                    {'username': ["A username already exist"]})
           
        return super(CreateUserForm, self).clean(*args, **kwargs)


class UserLoginForm(forms.Form):
    username = forms.CharField(label=False, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Username or Password incorrect')
            if not user.check_password(password):
                raise forms.ValidationError('Username or Password incorrect')
            if not user.is_active:
                raise forms.ValidationError('Username or Password incorrect')
        return super(UserLoginForm, self).clean(*args, **kwargs)

    class Meta():
        model = models.User
        fields = ('username', 'password')