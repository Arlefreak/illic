from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import *

class AdminImageMixin(object):
    def admin_image(self, obj):
        return u"<img src='%s' style='height: 100px; width: auto; display: block'/>" % obj.image.url
    admin_image.allow_tags = True
    admin_image.short_description = u"Preview"

@admin.register(Site)
class SiteAdmin(SingletonModelAdmin):
    pass

@admin.register(Therapy)
class TherapyAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = (
        'title',
        'small_text',
        'admin_image',
    )
    list_display_links = (
        'title',
        'small_text',
        'admin_image',
    )
