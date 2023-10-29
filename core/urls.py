from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('', views.home_view, name='home'),
    path('category/<int:category_id>/', views.category_view, name='category'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]