from cProfile import label
from random import choices
from wsgiref import headers
import django_filters
from . models import *



class FormFilter(django_filters.FilterSet):
    CHOICES= (
            ('first_name', 'First_name'),
            ('supervisor', ' Supervisor')
            )
      
    ordering = django_filters.ChoiceFilter(label="order_by", 
    choices=CHOICES, method="order")
    class Meta:
        model = Form
        fields = {
            'supervisor' :['icontains'],
            'department' :['icontains'],
            'university' :['icontains']
        }
      
    def order(self, queryset,name,  value):
        return queryset.order_by(value)