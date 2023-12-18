from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('', views.help_view, name='help'),
    path('home/', views.home_view, name='home'),
    path('category/<int:category_id>/', views.category_view, name='category'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('jobs/full-time/', views.full_time_jobs, name='full_time_jobs'),
    path('jobs/part-time/', views.part_time_jobs, name='part_time_jobs'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
]