from django import forms
from django.contrib.auth.decorators import login_required
from .models import Appointment, TIMESLOT_CHOICES
from datetime import date
from machines.models import Machines


class AppointmentForm(forms.ModelForm):

    """
    A form for booking an appointment, allowing users to select a treatment,
    date, and time. The form also collects additional information and ensures
    that selected dates are valid (not in the past, not on a Sunday, and not
    on a list of blocked dates).
    """
    appointment_date = forms.DateField(
        widget=forms.TextInput(attrs={
            'id': 'datepicker',
            'placeholder': 'Select a Date',
        }),
        label="Select a Date"
    )
    appointment_time = forms.ChoiceField(choices=TIMESLOT_CHOICES,
                                         label="Select a Time")

    class Meta:
        model = Appointment
        fields = ["name", "machine_selected", "appointment_date",
                  "appointment_time", "requests"]
        labels = {
            "name": "Your Name:",
            "machine_selected": "Select a machine:",
            "appointment_date": "Choose your preferred date:",
            "appointment_time": "Choose your preferred time:",
            "requests": "Additional information we should know:",
        }

    def clean_appointment_date(self):
        selected_date = self.cleaned_data.get("appointment_date")

        if selected_date < date.today():
            raise forms.ValidationError("You cannot select a past date.")

        if selected_date.weekday() == 6:
            raise forms.ValidationError(
                "Appointments cannot be booked on Sundays.")

        blocked_dates = [
            date(2024, 12, 24),
            date(2024, 12, 25),
            date(2024, 12, 26),
            date(2024, 12, 31),
            date(2025, 1, 1),
            date(2025, 2, 3),
            date(2025, 3, 17),
            date(2025, 4, 21),
            date(2025, 5, 5),
            date(2025, 6, 2),
            date(2025, 8, 4),
            date(2025, 10, 27),
            date(2025, 12, 24),
            date(2025, 12, 25),
            date(2025, 12, 26),
            date(2025, 12, 31),
        ]
        if selected_date in blocked_dates:
            raise forms.ValidationError(
                f"{selected_date} is not available. Please pick another date.")

        return selected_date
