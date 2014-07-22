from django.contrib import admin

from .models import Room
from field_application.account.models import Organization
from .models import Room, RoomApplication



class OrganizationAdmin(admin.ModelAdmin):
	pass


class RoomAdmin(admin.ModelAdmin):
     filter_horizontal = ('managers',)


class RoomApplicationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(RoomApplication, RoomApplicationAdmin)

