from django.contrib import admin
from moldslist.models import BPMSUser
@admin.register(BPMSUser)
class BPMSUserAdmin(admin.ModelAdmin):
    list_display = ('login', 'web_user')
