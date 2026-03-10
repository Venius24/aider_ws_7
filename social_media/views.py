from django.shortcuts import render
from .models import SocialMediaPost

def social_media_list(request):
    posts = SocialMediaPost.objects.all()
    return render(request, 'social_media/social_media_list.html', {'posts': posts})
