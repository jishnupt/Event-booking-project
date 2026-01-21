from django.contrib import admin
from .models import CustomUser,event_category,Events,EventBooking,Event_cancel

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(event_category)
admin.site.register(Events)
admin.site.register(EventBooking)
admin.site.register(Event_cancel)

