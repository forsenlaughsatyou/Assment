from django.contrib import admin
from .models import Employees,Qualifications,Projects,addressDetails,WorkExperience

# Register your models here.
admin.site.register(Employees)
admin.site.register(WorkExperience)
admin.site.register(Qualifications)
admin.site.register(Projects)
admin.site.register(addressDetails)