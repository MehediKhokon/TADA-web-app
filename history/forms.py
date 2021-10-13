from django import forms
from .models import Tada


class TadaForm(forms.ModelForm):
    DATEPICKER = {
        'type': 'text',
        'class': 'form-control',
        'id': 'datepicker'
    }
    date = forms.DateField(widget=forms.DateInput(attrs=DATEPICKER))
    class Meta:
        model = Tada
        fields = ('date', 'employee', 'travel_cost', 'lunch_cost', 'instruments_cost', 'paid',)
