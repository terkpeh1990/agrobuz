import django_filters
from django import forms
from django_filters import DateFilter , CharFilter, NumberFilter, MultipleChoiceFilter
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'


class BusinessFilter(django_filters.FilterSet):
    # object_status_list = ["Peasant Farmer", "Commercial Farmer"]
    # value_chain = MultipleChoiceFilter(field_name="value_chain", 
    #                         queryset= Value_Chain.objects.exclude(name__in =object_status_list).order_by('name')
    #                         )
    # Gender = MultipleChoiceFilter(field_name="bio__sex", 
    #                         queryset= Sex.objects.all().order_by('name')
    #                         )
       

    class Meta:
        model = Business_Info
        fields = ['value_chain', 'registration_status', 'type_ownership', 'scale','bio__sex'
                  ]


class AssociationFilter(django_filters.FilterSet):
    # object_status_list = ["Peasant Farmer", "Commercial Farmer"]
    # value_chain = MultipleChoiceFilter(field_name="value_chain", 
    #                         queryset= Value_Chain.objects.exclude(name__in =object_status_list).order_by('name')
    #                         )
    
    class Meta:
        model = Associations
        fields = ['value_chain', 'location',
                  ]

class AssociationFilter(django_filters.FilterSet):
    # object_status_list = ["Peasant Farmer", "Commercial Farmer"]
    # value_chain = MultipleChoiceFilter(field_name="value_chain", 
    #                         queryset= Value_Chain.objects.exclude(name__in =object_status_list).order_by('name')
    #                         )
    
    class Meta:
        model = Associations
        fields = ['value_chain', 'location',
                  ]

class BioFilter(django_filters.FilterSet):
    # value_chain = MultipleChoiceFilter(field_name="value_chain", 
    #                         queryset=Value_Chain.objects.exclude(name='Farmers').order_by('name')
    #                         )

    class Meta:
        model = Bio_Data
        fields = ['value_chain', 'location','sex',
                  ]



