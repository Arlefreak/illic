from django.conf.urls import url
from django_filters.views import FilterView

from .views import EntryDetailView, EntryListView
from .models import Entry

urlpatterns = [
    url(r'^$', EntryListView.as_view(), name='entry-list'),
    url(r'^entry/(?P<slug>[-\w]+)/$', EntryDetailView.as_view(), name='entry-detail'),
]
