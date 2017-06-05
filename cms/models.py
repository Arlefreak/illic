#!/usr/bin/env python
# -*- coding: utf-8 -*-from django.db import models

from django.db import models
from django.template import defaultfilters
from solo.models import SingletonModel
from ckeditor.fields import RichTextField
from adminsortable.models import SortableMixin


def upload_to(instance, filename):
    import os
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'uploads/%s%s%s' % (
        filename_base,
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),)

def upload_to_therapy(instance, filename):
    import os.path
    filename_base, filename_ext = os.path.splitext(filename)
    return 'therapy/%s%s' % (
        instance.slug,
        filename_ext.lower(),)

class Site(SingletonModel):
    title = models.CharField(max_length=140, default='Ilic')
    social_description = models.CharField(max_length=140, default='Social description')
    who = RichTextField('¿Quiénes somos?')
    when = RichTextField('¿Cuándo acudir a Terapia')
    phone = models.CharField(max_length=140)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=140)
    preview_image = models.ImageField(upload_to=upload_to)
    facebook = models.URLField(max_length=140, default='https://www.facebook.com/')
    twitter = models.URLField(max_length=140, default='https://twitter.com/')
    footer_message = models.CharField(max_length=140)
    def __str__(self):
        return 'Textos del sitio'
    class Meta:
        verbose_name = 'Textos del sitio'
        verbose_name_plural = 'Textos del sitio'

class Therapy(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    title = models.CharField(max_length=140, default='Terapia')
    slug = models.CharField(max_length=200, editable=False)
    text = RichTextField()
    small_text = models.CharField(max_length=140, default='Terapia')
    image = models.FileField(upload_to=upload_to_therapy)
    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        if self.pk is None:
            saved_image = self.image
            self.image = None
            super(Therapy, self).save(*args, **kwargs)
            self.image = saved_image
        super(Therapy, self).save(*args, **kwargs)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Terapia'
        verbose_name_plural = 'Terapias'
        ordering = ['order']
