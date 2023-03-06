
from django.urls import path,include

urlpatterns = [
    path('', include('smsapp.urls')),
    path('smsapp/', include('smsapp.urls')),

    
]
