from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import widgets


class DateInput(forms.DateInput):
    input_type = 'date'
    format = '%d.%m.%Y'

class RaitingDateForm(forms.Form):
    
    date = forms.DateField(widget=DateInput(
        {'class':'date_form','id':'date'}
    ))