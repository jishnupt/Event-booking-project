from django import forms
from .models import CustomUser,EventBooking,Events
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm


class UserRegForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','email']

class EventaddForm(forms.ModelForm):
    class Meta:
        model = Events
        exclude = ['admin_approval']

class EventBookingForm(forms.ModelForm):
    class Meta:
        model = EventBooking
        fields = ['event_date']
        widgets = {
            'event_date': forms.DateInput(attrs={
                'type': 'date',
                'min': timezone.now().date()
            })
        }

    def clean_event_date(self):
        event_date = self.cleaned_data['event_date']
        if event_date < timezone.now().date():
            raise forms.ValidationError("Past dates are not allowed.")
        return event_date