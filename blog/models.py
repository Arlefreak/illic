from django.db import models
from cms.models import Therapist
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from uuslug import uuslug

def upload_to_entry(instance, filename):
    import os.path
    filename_base, filename_ext = os.path.splitext(filename)
    return 'blog/entry/%s%s' % (
        instance.slug,
        filename_ext.lower(),)

class Entry(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=140, unique=True, editable=False)
    publish = models.BooleanField(default=True)
    text = RichTextField()
    social_description = models.CharField(max_length=140)
    tags = TaggableManager()
    author = models.ForeignKey(Therapist)
    image = models.FileField(upload_to=upload_to_entry, blank=True, null=True)
    dateCreated = models.DateField(auto_now_add=True, editable=False)
    dateUpdated = models.DateField(auto_now=True, editable=False)
    @models.permalink
    def get_absolute_url(self):
        return ('entry-detail', None, { 'slug': self.slug })
    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self, slug_field='slug')
        if self.pk is None:
            saved_image = self.image
            self.image = None
            super(Entry, self).save(*args, **kwargs)
            self.image = saved_image
        super(Entry, self).save(*args, **kwargs)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Blog Entry'
        verbose_name_plural = 'Blog Entries'
        ordering = ['-dateCreated']
