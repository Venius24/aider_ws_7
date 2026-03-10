from django.shortcuts import render
from .models import WebPage

def website_list(request):
    pages = WebPage.objects.all()
    return render(request, 'website/website_list.html', {'pages': pages})
