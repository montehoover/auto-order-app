from django.contrib import admin
from .models import ScheduledOrder

# allows ScheduledOrder objects to be managed from the Django Admin view
admin.site.register(ScheduledOrder)