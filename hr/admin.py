from django.contrib import admin
from .models import JobDescription, Recruitment, Area

admin.site.register(Area)
admin.site.register(JobDescription)
admin.site.register(Recruitment)