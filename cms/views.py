from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from .models import *

DEFAULT_TITLE = ''
DEFAULT_DESCRIPTION = ''
DEFAULT_PREVIEW = ''

def home(request):
    single = Site.get_solo()
    list = Therapy.objects.all()
    context = {
        'title' : single.title,
        'description': single.social_description,
        'preview': single.preview_image,
        'list': list,
        'single': single,
    }

    return render(request, 'home.html', context)
