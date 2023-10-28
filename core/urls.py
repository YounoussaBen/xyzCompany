from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]