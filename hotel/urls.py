from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact_view, name='contact_view'),
    path('success', views.success, name='success'),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    # Add other URL patterns as needed
]

