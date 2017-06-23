from django.contrib import admin
from .models import *

class ViewOnSiteMixin(object):
    def view_on_site_list(self, obj):
        return u"<a class='button' target='_blank' href='%s'>view on site</a>" % obj.get_absolute_url()
    view_on_site_list.allow_tags = True
    view_on_site_list.short_description = u"View on site"

class AdminImageMixin(object):
    def admin_image(self, obj):
        if(obj.image):
            return u"<img src='%s' style='height: 100px; width: auto; display: block'/>" % obj.image.url
        else:
            return u'NO IMAGE'
    admin_image.allow_tags = True
    admin_image.short_description = u"Preview"

@admin.register(Entry)
class EntryAdmin(ViewOnSiteMixin, admin.ModelAdmin, AdminImageMixin):
    view_on_site = True
    list_display = (
        'publish',
        'title',
        'author',
        'tag_list',
        'dateCreated',
        'admin_image',
        'view_on_site_list',
    )
    list_display_links = (
        'title',
        'tag_list',
        'dateCreated',
        'admin_image',
    )
    list_editable = (
        'author',
        'publish',
    )
    def get_queryset(self, request):
        return super(EntryAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
