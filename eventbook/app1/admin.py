from django.contrib import admin
from .models import CustomUser,event_category,Events,EventBooking

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(event_category)
admin.site.register(Events)
admin.site.register(EventBooking)

