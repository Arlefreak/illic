from django.shortcuts import render
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import *
from .filters import *
import django_filters

class EntryDetailView(DetailView):
    model = Entry
    template_name = 'entry_detail.html'
    def get_context_data(self, **kwargs):
        context = super(EntryDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class EntryListView(ListView):
    model = Entry
    template_name = 'entry_list.html'
    def get_context_data(self, **kwargs):
        f = EntryFilter(self.request.GET, queryset=Entry.objects.filter(publish=True))
        context = super(EntryListView, self).get_context_data(**kwargs)
        context['filter'] = f
        return context
