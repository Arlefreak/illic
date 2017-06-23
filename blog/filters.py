import django_filters
from .models import *
from taggit.managers import TaggableManager

class EntryFilter(django_filters.FilterSet):
    dateCreated = django_filters.DateRangeFilter(label='Fecha')
    author__slug = django_filters.CharFilter(label='Autor',)
    tags__name = django_filters.CharFilter(label='Tags')


    class Meta:
        model = Entry
        fields = {
            'dateCreated': [],
            'author__slug': [],
            'tags__name': [],
        }
