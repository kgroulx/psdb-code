from django.contrib import admin
from labs import models

class OrganizationAdmin(admin.ModelAdmin):
	pass
admin.site.register(models.Organization, OrganizationAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Appointment, AppointmentAdmin)
