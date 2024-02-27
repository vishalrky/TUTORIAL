import django_filters
from django_filters import CharFilter

from .models import *

class todoFilter(django_filters.FilterSet):
    todo_name= CharFilter(field_name='todo_name',lookup_expr='icontains')
    class Meta:
        model= todo
        fields= '__all__'
        exclude=['user','status']