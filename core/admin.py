from django.contrib import admin
from .models import Company, JobCategory, Job


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')


class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'vacancy')


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'deadline')
    list_filter = ('job_type', 'categories')
    search_fields = ('title', 'company__name', 'location')

admin.site.register(Company, CompanyAdmin)
admin.site.register(JobCategory, JobCategoryAdmin)
admin.site.register(Job, JobAdmin)
