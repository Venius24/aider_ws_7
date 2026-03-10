from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customers.urls')),
    path('feedback/', include('feedback.urls')),
    path('social_media/', include('social_media.urls')),
    path('website/', include('website.urls')),
    path('loyalty/', include('loyalty.urls')),
]
